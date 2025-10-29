"""
This script uses the News API library to retrieve news articles and compares them with data from the fbContentType.db database. 
It searches for similarities between Facebook ad content and news stories to help identify potential misinformation or related reports.
"""

""" Import necessary libraries and modules """
import sqlite3
import os
import requests
from newsapi import NewsApiClient
from difflib import SequenceMatcher
from facebookAd import FacebookAdScanner


# Database configuration
DB_NAME = 'fbContentType.db'


""" 
The NEW_API_SOURCES dictionary outlines various news API sources along with their corresponding API keys, 
allowing for seamless switching and fallback between different providers. 
"""
# Multiple News API sources configuration
# Configure your API keys below (get free keys from respective websites)
NEWS_API_SOURCES = {
    'newsapi_org': {
        'api_key': '7db691a7480b4488b8c544b417996e8a',  # NewsAPI.org (100 calls/day, 20 articles/call)
        'enabled': True,
        'url': 'https://newsapi.org'
    },
    'newsdata_io': {
        'api_key': 'pub_b67076ff2fb54340ae86b52ef2a65298',  # NewsData.io (500 calls/month, 10 articles/call)
        'enabled': True,
        'url': 'https://newsdata.io'
    },
    'thenewsapi': {
        'api_key': 'YOUR_THENEWSAPI_KEY',  # TheNewsAPI.com (1M articles/week)
        'enabled': False,
        'url': 'https://thenewsapi.com'
    },
    'worldnewsapi': {
        'api_key': 'b145d010d6ea49f796b95b719833d013',  # WorldNewsAPI.com (semantic tagging, sentiment)
        'enabled': True,
        'url': 'https://worldnewsapi.com'
    }
}


def get_db_connection(db_path=DB_NAME):
    """ Establishes a connection to the SQLite database. """
    return sqlite3.connect(db_path)


def fetch_content_from_database():
    """
    Retrieves all content from the fbContentType database and returns a list of 
    dictionaries containing file information and content.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT File_Name, Content_Info, Locations, Facebook_Ad, User_Content 
            FROM fbContentType
        ''')
        rows = cursor.fetchall()
        content_list = []
        scanner = FacebookAdScanner()
        for row in rows:
            file_name = row[0]
            # Try OCR if file exists
            ocr_text = None
            try:
                if file_name and os.path.exists(file_name):
                    ocr_text = scanner.basic_ocr(file_name)
            except Exception:
                ocr_text = None
            content_list.append({
                'file_name': file_name,
                'content_info': row[1],
                'ocr_text': ocr_text,
                'location': row[2],
                'is_facebook_ad': bool(row[3]),
                'is_user_content': bool(row[4])
            })
        return content_list

""" 
The fetch_media_content function scans a directory for media files, 
extracts text from images using OCR, and identifies potential Facebook ads based on their filenames. 
"""
def fetch_from_newsapi_org(query, api_key, language='en', page_size=20):
    """Fetch from NewsAPI.org"""
    try:
        newsapi = NewsApiClient(api_key=api_key)
        response = newsapi.get_everything(
            q=query,
            language=language,
            page_size=page_size,
            sort_by='relevancy'
        )
        return response.get('articles', [])
    except Exception as e:
        print(f"  ⚠️ NewsAPI.org error: {e}")
        return []


""" This function named fetch_from_newsdata_io fetches articles from NewsData.io API. """
def fetch_from_newsdata_io(query, api_key, language='en', page_size=10):
    """ Fetch from NewsData.io """
    try:
        url = f"https://newsdata.io/api/1/news?apikey={api_key}&q={query}&language={language}&page_size={page_size}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        articles = []
        for item in data.get('results', []):
            articles.append({
                'title': item.get('title', ''),
                'description': item.get('description', ''),
                'source': {'name': item.get('source_id', 'Unknown')},
                'url': item.get('link', ''),
                'publishedAt': item.get('pubDate', '')
            })
        return articles
    except Exception as e:
        print(f"  ⚠️ NewsData.io error: {e}")
        return []



""" This function named fetch_from_thenewsapi fetches articles from TheNewsAPI.com API and also handles errors. """
def fetch_from_thenewsapi(query, api_key, language='en', page_size=20):
    """Fetch from TheNewsAPI.com"""
    try:
        url = f"https://api.thenewsapi.com/v1/news/all?api_token={api_key}&search={query}&language={language}&limit={page_size}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        articles = []
        for item in data.get('data', []):
            articles.append({
                'title': item.get('title', ''),
                'description': item.get('description', ''),
                'source': {'name': item.get('source', 'Unknown')},
                'url': item.get('url', ''),
                'publishedAt': item.get('published_at', '')
            })
        return articles
    except Exception as e:
        print(f"  ⚠️ TheNewsAPI.com error: {e}")
        return []


""" The newsAPI.py function named fetch_from_worldnewsapi fetches articles from WorldNewsAPI.com API. """
def fetch_from_worldnewsapi(query, api_key, language='en', page_size=20):
    """Fetch from WorldNewsAPI.com"""
    try:
        url = f"https://api.worldnewsapi.com/search-news?api-key={api_key}&text={query}&language={language}&number={page_size}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        articles = []
        for item in data.get('news', []):
            articles.append({
                'title': item.get('title', ''),
                'description': item.get('text', '')[:200],
                'source': {'name': item.get('source_country', 'Unknown')},
                'url': item.get('url', ''),
                'publishedAt': item.get('publish_date', '')
            })
        return articles
    except Exception as e:
        print(f"  ⚠️ WorldNewsAPI.com error: {e}")
        return []


""" This function named fetch_news_articles fetches articles from multiple news API sources with fallback. """
def fetch_news_articles(query, language='en', page_size=20):
    """
    Fetches news articles from multiple sources with fallback.
    
    Parameters:
        query (str): The search query (keywords to search for).
        language (str): Language of the articles (default: 'en').
        page_size (int): Number of articles to fetch (default: 20).
        
    Returns:
        list: List of article dictionaries from all enabled sources.
    """
    all_articles = []
    sources_tried = []
    
    # Try each enabled source
    """ 
    The various if statements below check if each news API source is enabled. The if enabled block
    fetches articles from that source and appends them to the all_articles list. 
    """
    if NEWS_API_SOURCES['newsapi_org']['enabled']:
        sources_tried.append('NewsAPI.org')
        articles = fetch_from_newsapi_org(
            query, 
            NEWS_API_SOURCES['newsapi_org']['api_key'], 
            language, 
            page_size
        )
        all_articles.extend(articles)
    
    if NEWS_API_SOURCES['newsdata_io']['enabled']:
        sources_tried.append('NewsData.io')
        articles = fetch_from_newsdata_io(
            query, 
            NEWS_API_SOURCES['newsdata_io']['api_key'], 
            language, 
            min(page_size, 10)
        )
        all_articles.extend(articles)
    
    if NEWS_API_SOURCES['thenewsapi']['enabled']:
        sources_tried.append('TheNewsAPI.com')
        articles = fetch_from_thenewsapi(
            query, 
            NEWS_API_SOURCES['thenewsapi']['api_key'], 
            language, 
            page_size
        )
        all_articles.extend(articles)
    
    if NEWS_API_SOURCES['worldnewsapi']['enabled']:
        sources_tried.append('WorldNewsAPI.com')
        articles = fetch_from_worldnewsapi(
            query, 
            NEWS_API_SOURCES['worldnewsapi']['api_key'], 
            language, 
            page_size
        )
        all_articles.extend(articles)
    
    if sources_tried:
        print(f"  Searched: {', '.join(sources_tried)}")
    
    return all_articles


def calculate_similarity(text1, text2):
    """
    Calculates similarity ratio between two texts using SequenceMatcher.
    
    Parameters:
        text1 (str): First text string.
        text2 (str): Second text string.
        
    Returns:
        float: Similarity ratio (0.0 to 1.0).
    """
    return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()


def extract_keywords(content_info):
    """
    Extracts potential keywords from content info for News API search.
    
    Parameters:
        content_info (str): Content information text.
        
    Returns:
        list: List of keyword strings.
    """
    # Remove common words and extract meaningful keywords
    """ 
    The code includes a list of common words to filter from the content_info. 
    This is done to concentrate on more significant words that are likely to 
    produce better search results when querying news articles.
    """
    
    common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
                   'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had'}
    
    words = content_info.lower().replace(',', '').replace('.', '').replace('!', '').split()
    keywords = [word for word in words if word not in common_words and len(word) > 3]
    
    return keywords[:5]  # Return top 5 keywords


""" 
The function named cross_match_content_with_news matches database content with 
news articles from News API based on a specified similarity threshold.
"""
def cross_match_content_with_news(db_content_list, similarity_threshold=0.3):
    """
    Cross-matches database content with news articles from News API.
    
    Parameters:
        NEWS_API_KEY = 'YOUR_API_KEY_HERE'        NEWS_API_KEY = 'YOUR_API_KEY_HERE'        db_content_list (list): List of content dictionaries from database.
        similarity_threshold (float): Minimum similarity ratio to consider a match (0.0-1.0).
        
    Returns:
        list: List of matches with similarity scores.
    """
    """ Initialize empty list to hold matches. """
    matches = []

    """ 
    The for loop below iterates through each content item in the database's content list. 
    For each item, it extracts keywords, constructs a search query, fetches related news articles, and 
    compares the content with each article to calculate their similarity. 
    If the similarity exceeds the defined threshold, a match is recorded.
    """

    for content in db_content_list:
        print(f"\n{'='*80}")
        print(f"Analyzing: {content['file_name']}")
        print(f"Content: {content['content_info']}")
        if content.get('ocr_text'):
            print(f"OCR Text: {content['ocr_text'][:100]}")
        print(f"Type: {'Facebook Ad' if content['is_facebook_ad'] else 'User Content'}")
        # Use OCR text if available, else content_info
        search_text = content.get('ocr_text') or content['content_info']
        keywords = extract_keywords(search_text)
        query = ' '.join(keywords)
        print(f"Search keywords: {query}")
        # Fetch related news articles
        articles = fetch_news_articles(query)

        """ 
        An if block checks if any articles were returned from the fetch_news_articles function. 
        If no articles are found, it prints a message and continues to the next content item.
        """
        if not articles:
            print("No news articles found for this content.")
            continue
        print(f"Found {len(articles)} news articles. Analyzing similarities...")
        # Compare with each article
        for article in articles:
            article_title = article.get('title', '')
            article_description = article.get('description', '')
            article_text = f"{article_title} {article_description}"
            # Calculate similarity
            similarity = calculate_similarity(search_text, article_text)
            if similarity >= similarity_threshold:
                match = {
                    'db_content': content,
                    'news_article': {
                        'title': article_title,
                        'description': article_description,
                        'source': article.get('source', {}).get('name', 'Unknown'),
                        'url': article.get('url', ''),
                        'published_at': article.get('publishedAt', '')
                    },
                    'similarity_score': similarity
                }
                matches.append(match)
                print(f"  ✓ Match found! Similarity: {similarity:.2%}")
                print(f"    Article: {article_title[:60]}...")
    return matches



""" Based on the cross-matched results, this function displays the matches in a formatted manner. """
def display_matches(matches):
    """
    Displays the matched content and news articles in a formatted way.
    
    Parameters:
        matches (list): List of match dictionaries.
    """
    if not matches:
        print("\n" + "="*80)
        print("No matches found between database content and news articles.")
        return
    
    print("\n" + "="*80)
    print(f"SUMMARY: Found {len(matches)} match(es)")
    print("="*80)
    
    for i, match in enumerate(matches, 1):
        print(f"\n--- Match #{i} ---")
        print(f"Database File: {match['db_content']['file_name']}")
        print(f"DB Content: {match['db_content']['content_info']}")
        print(f"Type: {'Facebook Ad' if match['db_content']['is_facebook_ad'] else 'User Content'}")
        print(f"\nMatched News Article:")
        print(f"  Title: {match['news_article']['title']}")
        print(f"  Source: {match['news_article']['source']}")
        print(f"  Published: {match['news_article']['published_at']}")
        print(f"  URL: {match['news_article']['url']}")
        print(f"  Similarity Score: {match['similarity_score']:.2%}")
        print("-" * 80)



""" 
The main() function executes the news API cross-matching process. This also allows users to see
how the script works and what results it produces. 
"""
def main():
    """ Main function to run the news API cross-matching process. """
    print("="*80)
    print("NEWS API CONTENT MATCHER")
    print("="*80)
    print("This script compares content from fbContentType.db with news articles.\n")
    
    # Check if any API sources are enabled
    enabled_sources = [name for name, config in NEWS_API_SOURCES.items() if config['enabled']]
    
    if not enabled_sources:
        print("⚠️  WARNING: No News API sources enabled!")
        print("Please enable at least one API source and add your API key.")
        print("\nAvailable sources:")
        print("  1. NewsAPI.org - https://newsapi.org (100 calls/day)")
        print("  2. NewsData.io - https://newsdata.io (500 calls/month)")
        print("  3. TheNewsAPI.com - https://thenewsapi.com")
        print("  4. WorldNewsAPI.com - https://worldnewsapi.com")
        print("\nRunning in demo mode with database content only...\n")
        
        # Just display database content
        content_list = fetch_content_from_database()
        print(f"Found {len(content_list)} items in database:")
        for item in content_list:
            print(f"  - {item['file_name']}: {item['content_info'][:50]}...")
        return
    
    # Fetch content from database
    print("Step 1: Fetching content from database...")
    content_list = fetch_content_from_database()
    print(f"✓ Found {len(content_list)} items in database.\n")
    
    # Cross-match with news articles
    print("Step 2: Cross-matching with News API...")
    matches = cross_match_content_with_news(content_list, similarity_threshold=0.25)
    
    # Display results
    print("\n" + "="*80)
    print("Step 3: Displaying Results")
    display_matches(matches)
    
    print("\n" + "="*80)
    print("Analysis complete!")
    print("="*80)


""" 
The `if __name__ == '__main__':` block ensures that the `main()` function is called only when the script is 
executed directly, not when it is imported as a module into another script. This allows users to understand 
how the script works and the results it produces. This practice is common in Python programming.
"""
if __name__ == '__main__':
    main()

    
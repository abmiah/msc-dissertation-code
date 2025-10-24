""" 
This script provides functions to fetch news articles from various news APIs based on a given query. 
It begins by importing necessary libraries and the NewsArticle model. The script defines individual functions to fetch
articles from NewsAPI.org, NewsData.io, TheNewsAPI, and WorldNewsAPI. Each function handles API requests, processes responses, and returns a list of NewsArticle objects.
The main function, fetch_news_articles, aggregates articles from all enabled sources based on the provided query. 
"""
from typing import List
from newsapi import NewsApiClient
from .config import LANGUAGE, PAGE_SIZE
from .models import NewsArticle
import os

# Import NEWS_API_SOURCES from the main newsAPI.py for now (could be moved to config)
""" This will import NEWS_API_SOURCES from newsAPI module if available, otherwise initializes it as an empty dictionary. 
This allows the script to function even if the newsAPI module is not present, providing a fallback mechanism. 
This is also wrapped around an try-except block to handle the potential ImportError. """
try:
    from newsAPI import NEWS_API_SOURCES
except ImportError:
    NEWS_API_SOURCES = {}


""" the fetch_from_newsapi_org function fetches news articles from NewsAPI.org using the provided query and API key. 
It processes the API response and returns a list of NewsArticle objects. """
def fetch_from_newsapi_org(query, api_key, language=LANGUAGE, page_size=PAGE_SIZE):

    """ The block is wrapped in a try-except to handle any exceptions that may occur during the API request or processing."""
    try:
        newsapi = NewsApiClient(api_key=api_key)
        response = newsapi.get_everything(
            q=query,
            language=language,
            page_size=page_size,
            sort_by='relevancy'
        )
        articles = []
        for a in response.get('articles', []):
            articles.append(NewsArticle(
                title=a.get('title', ''),
                description=a.get('description', ''),
                source=(a.get('source') or {}).get('name', 'Unknown'),
                url=a.get('url', ''),
                published_at=a.get('publishedAt', ''),
            ))
        print(f"  ✓ NewsAPI.org: Found {len(articles)} articles")
        return articles
    except Exception as e:
        print(f"  ⚠️ NewsAPI.org error: {e}")
        return []

""" The function name fetch_from_newsdata_io fetches news articles from NewsData.io using the provided query and API key. 
It processes the API response and returns a list of NewsArticle objects. This also import requests library for making HTTP requests. 
The try-except block is used to handle any exceptions that may occur during the API request or processing. """
def fetch_from_newsdata_io(query, api_key, language=LANGUAGE, page_size=10):
    import requests
    try:
        # NewsData.io uses 'size' parameter, not 'page_size'
        url = f"https://newsdata.io/api/1/news?apikey={api_key}&q={query}&language={language}&size={page_size}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # Check for API errors
        if data.get('status') == 'error':
            error_msg = data.get('results', {}).get('message', 'Unknown error') if isinstance(data.get('results'), dict) else 'Unknown error'
            print(f"  ⚠️ NewsData.io error: {error_msg}")
            return []
            
        articles = []
        for item in data.get('results', []):
            articles.append(NewsArticle(
                title=item.get('title', ''),
                description=item.get('description', ''),
                source=item.get('source_id', 'Unknown'),
                url=item.get('link', ''),
                published_at=item.get('pubDate', '')
            ))
        print(f"  ✓ NewsData.io: Found {len(articles)} articles")
        return articles
    except Exception as e:
        print(f"  ⚠️ NewsData.io error: {e}")
        return []

""" This function processes the API response and returns a list of NewsArticle objects, 
also imports the requests library for making HTTP requests. """
def fetch_from_thenewsapi(query, api_key, language=LANGUAGE, page_size=PAGE_SIZE):
    import requests

    """ The try-except block is used to handle any exceptions that may occur during the API request or processing. """
    try:
        url = f"https://api.thenewsapi.com/v1/news/all?api_token={api_key}&search={query}&language={language}&limit={page_size}"
        response = requests.get(url, timeout=10)
        data = response.json()
        articles = []
        for item in data.get('data', []):
            articles.append(NewsArticle(
                title=item.get('title', ''),
                description=item.get('description', ''),
                source=item.get('source', 'Unknown'),
                url=item.get('url', ''),
                published_at=item.get('published_at', '')
            ))
        return articles
    except Exception:
        return []


""" This function fetches news articles from WorldNewsAPI using the provided query and API key. 
It processes the API response and returns a list of NewsArticle objects. This also import requests library for making HTTP requests. 
This also uses a try-except block to handle any exceptions that may occur during the API request or processing. """
def fetch_from_worldnewsapi(query, api_key, language=LANGUAGE, page_size=PAGE_SIZE):
    import requests
    try:
        url = f"https://api.worldnewsapi.com/search-news?api-key={api_key}&text={query}&language={language}&number={page_size}"
        response = requests.get(url, timeout=10)
        data = response.json()
        articles = []
        for item in data.get('news', []):
            articles.append(NewsArticle(
                title=item.get('title', ''),
                description=item.get('text', '')[:200],
                source=item.get('source_country', 'Unknown'),
                url=item.get('url', ''),
                published_at=item.get('publish_date', '')
            ))
        print(f"  ✓ WorldNewsAPI: Found {len(articles)} articles")
        return articles
    except Exception as e:
        print(f"  ⚠️ WorldNewsAPI error: {e}")
        return []


""" The final function fetch_news_articles aggregates articles from all enabled sources based on the provided query. 
It has several if statements to check which sources are enabled in NEWS_API_SOURCES """
def fetch_news_articles(query: str) -> List[NewsArticle]:
    """
    Fetches news articles from all enabled sources in NEWS_API_SOURCES.
    """
    all_articles = []
    if not NEWS_API_SOURCES:
        # fallback to NewsAPI.org with config key if NEWS_API_SOURCES not found
        from .config import NEWS_API_KEY
        return fetch_from_newsapi_org(query, NEWS_API_KEY)
    if NEWS_API_SOURCES.get('newsapi_org', {}).get('enabled'):
        all_articles.extend(fetch_from_newsapi_org(query, NEWS_API_SOURCES['newsapi_org']['api_key']))
    if NEWS_API_SOURCES.get('newsdata_io', {}).get('enabled'):
        all_articles.extend(fetch_from_newsdata_io(query, NEWS_API_SOURCES['newsdata_io']['api_key']))
    if NEWS_API_SOURCES.get('thenewsapi', {}).get('enabled'):
        all_articles.extend(fetch_from_thenewsapi(query, NEWS_API_SOURCES['thenewsapi']['api_key']))
    if NEWS_API_SOURCES.get('worldnewsapi', {}).get('enabled'):
        all_articles.extend(fetch_from_worldnewsapi(query, NEWS_API_SOURCES['worldnewsapi']['api_key']))
    return all_articles
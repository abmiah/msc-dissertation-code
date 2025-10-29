""" 
Main script to load content items, enrich with OCR, fetch news articles, 
and match them with news articles. This serves as the application entry point.
"""

""" 
The initial import statements are crucial as they bring in the necessary modules and functions from other parts of the 
application. These imports ensure that the pipeline operates correctly by providing access to various functionalities 
such as database operations, OCR processing, news fetching, and matching logic. Some of the imported modules also include 
data models and configuration settings, while others are imported for future use or to maintain consistency throughout 
the application. Specifically, the statement `from app import db, ocr, news, match` imports the `db`, `ocr`, `news`, and 
`match` modules from the app package, which is organized within the same project structure.
"""
from app import db, ocr, news, match
from app.models import ContentItem
from app.config import NEWS_API_KEY


""" 
The `run_pipeline()` function coordinates the complete process of loading content items from the database, 
enhancing them with OCR data, retrieving related news articles, and matching these content items with the news 
articles. Additionally, this function manages the display of results, which includes both matched items and 
unmatched items that could suggest potential misinformation. 
"""

""" 
When the function is excuted, it performs the following steps:
1. Loads content items from the database using db.fetch_content_items().
2. Enriches the loaded items with OCR data using ocr.enrich_with_ocr().
3. Fetches related news articles and matches them with the content items using match.match_items_with_news().
4. Displays the matched items along with their similarity scores and article details.
5. Identifies and reports any unmatched items as potential false information.
"""

def run_pipeline():
    """ Orchestrates the entire verification pipeline: load data, enrich with OCR, fetch news, and match. """
    print("Loading items from DB...")
    items = db.fetch_content_items()
    print(f"Loaded {len(items)} items.")

    print("Enriching with OCR (if files exist)...")
    items = ocr.enrich_with_ocr(items)

    print("Fetching related news and matching from all enabled APIs...")
    matches = match.match_items_with_news(items, news.fetch_news_articles)

    # Track which items have matches (by item object, not filename)
    matched_items = {id(m.item) for m in matches}
    
    print("="*80)
    print(f"\nFound {len(matches)} matches:")
    print("="*80)
    for i, m in enumerate(matches, 1):
        print(f"\nMatch #{i} | score={m.similarity:.2%}")
        print(f" - File: {m.item.file_name}")
        print(f" - Content: {m.item.content_info[:80]}")
        if m.item.ocr_text:
            print(f" - OCR Text: {m.item.ocr_text[:80]}")
        print(f" - Article: {m.article.title}")
        print(f" - Source: {m.article.source}")
        print(f" - URL: {m.article.url}")
    
    # Report items without matches as potential false information
    """ 
    For any content items that do not match any news articles, the function identifies them as potential 
    false information. This is accomplished by checking which items are absent from the matched_items set 
    and printing their details along with a cautionary message.
    """
    unmatched_items = [item for item in items if id(item) not in matched_items]
    if unmatched_items:
        print(f"\n{'='*80}")
        print(f"UNMATCHED ITEMS ({len(unmatched_items)}):")
        print("="*80)
        for item in unmatched_items:
            print(f"\n⚠️  File: {item.file_name}")
            print(f"   Content: {item.content_info[:80]}")
            print(f"   Status: The information from this post cannot be verified❗️, please be cautious of potential misinformation.")
            print(f"\n{'-'*80}")



""" 
The `if __name__ == '__main__':` block ensures the `main()` function runs only when the script is executed directly, 
not when imported as a module. This practice is common in Python programming, allowing users to see how the script works.
"""
if __name__ == '__main__':
    run_pipeline()

    
""" 
Main pipeline script to load content items, enrich with OCR, fetch news articles, 
and match content items with news articles. This is also the entry point of the application. 
"""

""" 
The initial import statements bring in necessary modules and functions from other parts of the application. 
These imports are essential for the pipeline to function correctly, as they provide access to database operations, 
OCR processing, news fetching, and matching logic. Some of the imported modules also include data models and configuration 
settings. and others are imported for future use or to maintain consistency across the application. 
The from app import db, ocr, news, match statement imports the db, ocr, news, and match modules from the app package, 
which is based within the same project structure.
"""
from app import db, ocr, news, match
from app.models import ContentItem
from app.config import NEWS_API_KEY


""" The run_pipeline() function orchestrates the entire process of loading content items from the database,
enriching them with OCR data, fetching related news articles, and matching the content items with the news articles. 
This function also handles the display of results, including matched items and unmatched items that may indicate 
potential misinformation. """

""" When the function is excuted, it performs the following steps:
1. Loads content items from the database using db.fetch_content_items().
2. Enriches the loaded items with OCR data using ocr.enrich_with_ocr().
3. Fetches related news articles and matches them with the content items using match.match_items_with_news().
4. Displays the matched items along with their similarity scores and article details."""

def run_pipeline():
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
    """ For any content items that did not find a match in the news articles,
    the function reports them as potential false information. This is done by checking
    which items were not included in the matched_items set and printing their details
    along with a cautionary message. """
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



""" The if __name__ == '__main__': block ensures that the main() function is called only when the script is run directly,
and not when it is imported as a module in another script. This allows users to see how the script works and what results 
it produces. This is also common practice in Python programming. """
if __name__ == '__main__':
    run_pipeline()

""" 
The `app/match.py` module provides functionality for matching content items with news articles based on their textual similarity. 
It begins by importing the necessary libraries and the data models used in the application.

The module defines functions to extract keywords from text, calculate similarity scores, and match content items with news 
articles from various sources. The matching process involves querying news APIs using the keywords extracted from the content 
items and comparing the text of these items with the titles and descriptions of the fetched news articles. If the similarity 
score exceeds a defined threshold, a match is recorded.

Additionally, the script imports the `SequenceMatcher` class from the `difflib` module to compute similarity ratios between 
strings, as well as the `List` type from the `typing` module for type hinting.
"""

from difflib import SequenceMatcher
from typing import List
from .models import ContentItem, NewsArticle, MatchResult
from .config import SIMILARITY_THRESHOLD


""" 
The extract_keywords function identifies significant keywords from a text by removing common words and limiting the number 
of keywords returned. This function helps in forming effective search queries to find news articles relevant to the content.
"""
def extract_keywords(text: str) -> str:
    """ Extracts significant keywords from text by removing common words. """
    common = {
        'the','a','an','and','or','but','in','on','at','to','for','is','are','was','were','be','been','being','have','has','had'
    }
    words = text.lower().replace(',', ' ').replace('.', ' ').replace('!', ' ').split()
    keywords = [w for w in words if w not in common and len(w) > 3]
    return ' '.join(keywords[:5])


""" 
The similarity function computes a similarity score between two input strings by utilizing the SequenceMatcher 
class from the difflib module. It returns a float value that indicates the similarity ratio between the two strings. 
This score is useful for assessing how closely the content item matches a news article.
"""
def similarity(a: str, b: str) -> float:
    """ Computes a similarity score between two strings using SequenceMatcher. """
    return SequenceMatcher(None, (a or '').lower(), (b or '').lower()).ratio()


""" 
The `match_items_with_news` function is designed to match a list of `ContentItem` objects with news articles gathered
from a specified fetcher function. It iterates through each content item, extracts keywords to formulate a search query,
and retrieves news articles related to that query. The function then compares the text of each content item with the
titles and descriptions of the retrieved news articles, calculating a similarity score for each comparison. If the similarity 
score exceeds a predefined threshold, a `MatchResult` object is created and added to a results list. Ultimately, the function 
returns a list of `MatchResult` objects that represent the successful matches.
"""
def match_items_with_news(items: List[ContentItem], fetcher) -> List[MatchResult]:
    """ Matches content items with news articles using similarity scoring. """
    results: List[MatchResult] = []
    for item in items:
        # ONLY use Content_Info from database (or OCR text if available)
        # Never match on filename
        base_text = item.ocr_text or item.content_info
        if not base_text or not base_text.strip():
            continue
        
        # Extract keywords from content only
        query = extract_keywords(base_text)
        if not query:
            continue
        
        print(f"\n  Searching for: '{query}' (from {item.file_name})")
        articles = fetcher(query)
        print(f"  Retrieved {len(articles)} articles total")
        
        for art in articles:
            # Compare content with news article title and description only
            score = similarity(base_text, f"{art.title} {art.description}")
            if score >= SIMILARITY_THRESHOLD:
                results.append(MatchResult(item=item, article=art, similarity=score))
                print(f"    ✓ Match! Score: {score:.2%} - {art.title[:60]}")
    return results
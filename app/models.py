""" The app/models.py module defines data models used in the application,
including ContentItem, NewsArticle, and MatchResult. These models are implemented
as dataclasses to facilitate easy storage and manipulation of related data attributes."""

from dataclasses import dataclass
from typing import Optional

""" 
The @dataclass decorator is used to automatically generate special methods for the class,
such as __init__() and __repr__(), based on the defined attributes. 

The class ContentItem defined below represent the core data structures used throughout the application:
- ContentItem: Represents a content item with attributes such as file_name, content_info, location,
  is_facebook_ad, is_user_content, and an optional ocr_text for storing OCR results.
- NewsArticle: Represents a news article with attributes like title, description, source, url, and published_at.
- MatchResult: Represents the result of matching a ContentItem with a NewsArticle, including the similarity score.
"""
@dataclass
class ContentItem:
    file_name: str
    content_info: str
    location: str
    is_facebook_ad: bool
    is_user_content: bool
    ocr_text: Optional[str] = None


""" The class NewsArticle represents a news article with attributes such as title, description, source, url, and published_at. 
This is also implemented as a dataclass. The @dataclass decorator is used to automatically generate special methods for the class,
such as __init__() and __repr__(), based on the defined attributes."""
@dataclass
class NewsArticle:
    title: str
    description: str
    source: str
    url: str
    published_at: str


""" The last class MatchResult represents the result of matching a ContentItem with a NewsArticle, including the similarity score. 
This is also implemented as a dataclass. The @dataclass decorator is used to automatically generate special methods for the class,
such as __init__() and __repr__(), based on the defined attributes. """
@dataclass
class MatchResult:
    item: ContentItem
    article: NewsArticle
    similarity: float

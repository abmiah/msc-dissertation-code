""" 
The app/models.py module defines the data models used in the application, which include ContentItem, 
NewsArticle, and MatchResult. These models are structured as dataclasses to simplify the storage and 
manipulation of related data attributes.
"""

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


"""
The `NewsArticle` class represents a news article and includes attributes such as title, description, source, URL, and publication date. 
It is implemented as a dataclass, using the `@dataclass` decorator to automatically generate special methods for the class, including 
`__init__()` and `__repr__()`, based on the defined attributes.
"""
@dataclass
class NewsArticle:
    title: str
    description: str
    source: str
    url: str
    published_at: str


""" 
The final class, `MatchResult`, represents the outcome of matching a `ContentItem` with a `NewsArticle`, including a similarity score. 
This class is implemented as a data class. The `@dataclass` decorator is utilized to automatically generate special methods for the 
class, such as `__init__()` and `__repr__()`, based on the specified attributes.
"""
@dataclass
class MatchResult:
    item: ContentItem
    article: NewsArticle
    similarity: float



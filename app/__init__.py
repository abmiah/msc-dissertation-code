"""
app package
=====================================

This package contains the core modules used by the Facebook Ad Content
Verification System. It is intentionally lightweight: no runtime logic is
executed at import time. The purpose of this file is to mark the directory as a
Python package and provide a concise overview of the available submodules.

Modules
-------
- config: Global configuration constants (e.g., DB_NAME, SCAN_DIRECTORY,
	NEWS_API_KEY, SIMILARITY_THRESHOLD, PAGE_SIZE, LANGUAGE).
- db: Database helpers for SQLite (connections, queries, and simple CRUD).
- models: Data models used across the app (e.g., NewsArticle).
- ocr: OCR pipeline built on Tesseract with image pre-processing utilities.
- news: Multi-source news fetching and aggregation utilities integrating
	NewsAPI.org, NewsData.io, TheNewsAPI, and WorldNewsAPI.
- match: Similarity and matching utilities for comparing extracted content
	against news articles.

Typical imports
---------------
- from app.news import fetch_news_articles
- from app.ocr import extract_text_from_image  # if defined in ocr.py
- from app.match import ...                    # matching helpers

Note
----
Keep this file minimal to avoid circular imports and side effects. Prefer
importing directly from the specific submodule you need (e.g., app.news,
app.ocr) rather than relying on package-level re-exports.
"""

# Public submodules for static analysis and auto-completion tools
__all__ = [
		"config",
		"db",
		"models",
		"ocr",
		"news",
		"match",
]

# Optional, lightweight package metadata
__version__ = "0.1.0"


# News API Setup Guide and Overview

# 1. Introduction
The `newsAPI.py` script constitutes a critical component of the Facebook Ad Content Verification System, functioning as an independent analytical tool designed to validate the integrity of advertisement content. This script systematically retrieves textual data from Facebook advertisements through optical character recognition (OCR) techniques, with the data stored within an SQLite database. Subsequently, it extracts pertinent keywords and executes queries across multiple news APIs—including NewsAPI.org, NewsData.io, WorldNewsAPI, and optionally TheNewsAPI—to identify relevant journalistic articles. Utilizing Python's `difflib.SequenceMatcher`, the script calculates similarity scores that facilitate the detection of potential correlations between ad content and reputable news sources, thereby assisting in the identification of misinformation. The system supports both automated processing workflows and manual troubleshooting procedures, offering comprehensive output that encompasses similarity metrics, article titles, sources, and URLs. The accompanying setup guide details procedures for configuring API keys and executing the script effectively.

# 2. Overview
The `newsAPI.py` script compares content from the `fbContentType.db` database with real news articles fetched from News API to identify potential matches or misinformation.

## Features
- ✅ Fetches content from the database
- ✅ Extracts keywords from content
- ✅ Searches News API for related articles
- ✅ Calculates similarity scores between content and articles
- ✅ Displays matches with similarity percentages

# 3. Setup Instructions

To configure the `newsAPI.py` script appropriately, users must first acquire API keys from one or more news data providers. These keys can be obtained by registering for free accounts on the providers' official websites, such as NewsAPI.org, NewsData.io, and WorldNewsAPI. Most of these services offer comprehensive free tiers suitable for research and testing purposes. After registration, users should copy the API keys provided on each dashboard. The next step involves opening the `newsAPI.py` script in a preferred code editor, with Visual Studio Code being recommended. Within the script, locate the `NEWS_API_SOURCES` dictionary, typically found between lines 18 and 40. Users should replace placeholder strings like `'YOUR_NEWSAPI_ORG_KEY'` with their actual API keys and activate individual providers by setting `'enabled': True`. It is imperative to enable at least one provider, as the script consolidates results from all active sources. Finally, save the modifications, activate the relevant virtual environment, and execute the script using the command `python newsAPI.py`.

## 1. Get a News API Key (Free)
1. Visit: https://newsapi.org
2. Click "Get API Key" or "Sign Up"
3. Create a free account
4. Copy your API key

## 2. Configure the Script
Open `newsAPI.py` and find this line (around line 15):
```python
NEWS_API_KEY = 'YOUR_API_KEY_HERE'
```

Replace `'YOUR_API_KEY_HERE'` with your actual API key:
```python
NEWS_API_KEY = 'abc123def456...'  # Your actual key
```

## 3. Run the Script
```bash
python newsAPI.py
```

# 4. How It Works

The `newsAPI.py` script facilitates a comprehensive process integrating database content with global journalistic sources. Initially, it establishes a connection to an SQLite database to extract all stored data entries, including Optical Character Recognition (OCR)-derived text from images and videos. Subsequently, the script analyzes each data item to determine salient keywords by systematically removing common stop words such as "the," "is," and "and." The most relevant terms are identified as those that optimally encapsulate the content. These keywords function as search queries dispatched concurrently to all activated news Application Programming Interfaces (APIs). The script further standardizes the heterogeneous API responses into a coherent, unified format, enabling the aggregation of articles from multiple sources. It then employs character-based sequence matching to compare database content with article titles and descriptions, thereby computing similarity scores. Articles surpassing a predefined similarity threshold—configurable within a range of 15-25%—are reported with comprehensive metadata, including publication dates, sources, and verification URLs, thereby assisting users in assessing content authenticity and detecting misinformation.

1. **Database Content Extraction**: Reads all entries from `fbContentType.db`
2. **Keyword Extraction**: Extracts meaningful keywords from each content entry
3. **News API Search**: Searches for news articles using those keywords
4. **Similarity Calculation**: Compares content with article titles and descriptions
5. **Match Reporting**: Reports matches above the similarity threshold (default: 25%)

# 5. Customization

## Adjust Similarity Threshold
In the `main()` function, change the `similarity_threshold` parameter:
```python
matches = cross_match_content_with_news(content_list, similarity_threshold=0.30)
```
- Lower values (e.g., 0.15) = more matches, less strict
- Higher values (e.g., 0.50) = fewer matches, more strict

## Change Number of Articles
In `fetch_news_articles()` function:
```python
def fetch_news_articles(query, api_key=NEWS_API_KEY, language='en', page_size=50):
```

## Example Output

```
================================================================================
Analyzing: hello_kitty.jpg
Content: Hello Kitty is come to town!, Book now for your exclusive offers.
Type: Facebook Ad
Search keywords: hello kitty town book exclusive offers

Found 15 news articles. Analyzing similarities...
  ✓ Match found! Similarity: 32.45%
    Article: Hello Kitty Exhibition Opens in London - Book Tickets Now...

--- Match #1 ---
Database File: hello_kitty.jpg
DB Content: Hello Kitty is come to town!, Book now for your exclusive offers.
Type: Facebook Ad

Matched News Article:
  Title: Hello Kitty Exhibition Opens in London - Book Tickets Now
  Source: BBC News
  Published: 2025-10-15T10:30:00Z
  URL: https://bbc.com/news/hello-kitty-exhibition
  Similarity Score: 32.45%
```

## Dependencies
- `newsapi-python` (installed via pip)
- `sqlite3` (built-in)
- `difflib` (built-in)

## Notes
- Free News API accounts have rate limits (100 requests/day for Developer plan)
- Articles are sorted by relevancy
- Only searches articles from the last month by default
- Works with both Facebook Ads and User Content from the database

## Troubleshooting

### "Import newsapi could not be resolved"
Install the package:
```bash
pip install newsapi-python
```

### "Error fetching news articles: API key invalid"
- Check that you've replaced `'YOUR_API_KEY_HERE'` with your actual key
- Verify your key is active at https://newsapi.org/account

### "No matches found"
- Lower the similarity threshold
- Check that your database has content (`sqlite3 fbContentType.db "SELECT * FROM fbContentType;"`)
- Try more generic keywords


---

# 6. Summary
The `newsAPI.py` script functions as a standalone diagnostic instrument within the Facebook Ad Content Verification System, facilitating rapid cross-verification of advertising content against a diverse array of credible news sources. By integrating multiple news APIs—including, but not limited to, NewsAPI.org, NewsData.io, WorldNewsAPI, and optionally TheNewsAPI—it enhances robustness against rate limitations and service outages, thereby enabling comprehensive journalistic source coverage. The application employs sophisticated keyword extraction and similarity algorithms to optimize the balance between recall and precision, effectively identifying potential misinformation while minimizing false positive rates. Its detailed output—comprising similarity metrics, article metadata, and verification hyperlinks—supports both manual review processes and automated workflows, rendering it suitable for academic, policy-making, and cybersecurity contexts. The modular architecture permits autonomous operation or seamless incorporation into the primary pipeline (`main.py`). Featuring adjustable thresholds, multi-source data aggregation, and transparent reporting mechanisms, this tool offers a practical approach to combating digital misinformation through transparent and reproducible verification methodologies.
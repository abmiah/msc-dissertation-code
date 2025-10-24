# 1. Introduction 
This README outlines a hypothetical mitigation strategy to counter misinformation on social media, with a particular focus on Facebook. Over the preceding year, there have been numerous instances of misinformation that have influenced user behaviour and targeted specific psychological predispositions. Of particular interest is the susceptibility of individuals exhibiting high levels of Neuroticism to microtargeting campaigns. Such individuals tend to display behavioural traits characterised by persistent negative emotions, including anxiety, self-consciousness, anger, impulsivity, and hostility. Additionally, they often demonstrate poor impulse control and heightened stress reactivity. Conversely, individuals with low levels of Neuroticism generally exhibit traits of calmness, self-possession, and even-temperedness (Dam et al., 2021; Lim, 2025; Sutton, 2025)
During the preliminary phase of the written study involving UK participants, the results revealed that individuals with elevated levels of Neuroticism exhibit increased susceptibility to microtargeted advertisements, primarily due to heightened emotional fear responses that subsequently trigger behavioural reactions. These findings align with existing research supported by Bakir (2020) and Prichard (2021), which emphasises the vulnerability of specific populations to digital influence.
The dissemination of misinformation presents significant implications in the digital era, especially given the rapid and pervasive nature of information spread facilitated by social media platforms such as Facebook, which boasts over three billion active users (Dixon, 2025c). Facebook also collects extensive data on its users, including behavioural patterns, social network connections, product usage, transactional activities on the platform, and analyses of user interactions within their networks, primarily for targeted advertising (Meta, 2022).
Companies and governmental agencies can utilise Facebook's advertising platform, leveraging micro-targeting to customise ads based on specific demographic parameters, such as location and gender. Nonetheless, the ethical implications of such targeted advertising remain a subject of debate, particularly given the lack of oversight concerning the potential dissemination of misinformation. Furthermore, it has been alleged that entities like Cambridge Analytica exerted influence over various political campaigns, including the deployment of targeted advertisements that purportedly contributed to Donald J. Trump's electoral victory in the 2016 United States presidential election, wherein he secured 304 electoral votes compared to Hillary Clinton's 227. (History.com Editors, 2018; The New York Times, 2017) Alongside other political campaigns from Australia, several African nations, as well as Mexico, Brazil, India, and Malaysia, have employed digital microtargeting strategies for purposes of political and social manipulation (BBC News, 2018b; Netflix, 2019; Nyabola, 2019; SBS News, 2018). This indicates that microtargeting and data-driven misinformation are not restricted to specific regions or cultural contexts but are progressively emerging as global trends.

## Please Note: Code execution is purely hypothetical 
This coding framework is purely hypothetical; consequently, it is not possible to conduct a live scan on Facebook's actual system due to the lack of academic access. The code references previous advertisements on Facebook that have raised ethical concerns related to misinformation.

# 2. Current Situation as of the present analysis. 
The UK’s Online Safety Act 2023 seeks to establish a regulatory framework aimed at controlling and mitigating harmful online content, with a particular emphasis on addressing the proliferation of misinformation across social media platforms. (Legislation.Gov.UK, 2023),  misinformation contributed to a violent riot that took place on July 29, 2024, sparked by claims that a Muslim asylum seeker was involved in a brutal attack at a dance studio in Southport. The spread of false information on social media reached millions of users. The individual was later identified as a British national with no links to Islam nor any status as an illegal immigrant. While this does not implicate the individual in the violent act, the ensuing demonstrations resulted in clashes with law enforcement personnel, with some demonstrators blaming asylum seekers and the Muslim community. It can be argued that social media platforms failed to adequately address the dissemination of misinformation; in fact, there are claims that Facebook’s algorithms may have even amplified such content due to high engagement levels (BBC Bitesize, 2024; Benesch, 2021; Fung, 2024; Kiderlin, 2024; Mohamed, 2024; Shah, 2024). According to Woods (2024), the legislation itself fails to directly address the issue of misinformation, primarily due to the absence of clearly defined criteria for criminality and intent.

# 3. Methodology 
A software tool could be integrated into social media platforms such as Facebook and other relevant networks to enhance the detection of misinformation. This approach would leverage UK-specific initiatives to combat disinformation by cross-referencing advertisements and viral posts via a news API. Nonetheless, this endeavour faces several challenges, including issues of platform confidentiality and the necessity for collaboration between platform providers and government agencies. The primary objective is to mitigate the spread of misinformation by alerting users to verify content, providing credible sources, and assisting in classifying information as factual or otherwise.    

# 4. Mitigation Hypothesis
To effectively combat the proliferation of misinformation, it is imperative to develop an automated, independent third-party tool. Such a tool should be seamlessly integrated into social media platforms to facilitate the verification of advertisements' authenticity and enable the identification of potential misinformation prior to its dissemination. This approach aims to enhance the integrity of information circulated within digital environments, supporting stakeholders such as users, researchers, and regulatory authorities. 
This research presents a modular, Python-based framework designed to address the pervasive issue of misinformation within online advertising. The system employs advanced Optical Character Recognition (OCR) (Lee, 2022) techniques to analyse visual media, such as images and videos, to extract textual content. This extracted data is systematically stored within a structured database, facilitating efficient retrieval and analysis. Subsequently, the framework utilises public news APIs to cross-reference the extracted information against reputable news sources.
By quantifying the similarity between ad content and verified journalistic articles, the system can identify and flag potentially unverified or false information. In a simulated environment, the methodology involves analysing local media files from a user's Facebook domain to extract and compare textual content with established news narratives. The modular architecture of the system allows for seamless integration of additional APIs, scalability to accommodate diverse data sources, and adaptability to real-world datasets. This approach contributes to broader efforts to combat misinformation in digital advertising and serves as a foundational tool for research on digital literacy, cybersecurity, and policy development.
# 5. Facebook Ad Content Verification System
This Python-based system is designed to detect and authenticate Facebook advertisements through comparative analysis of their content against reputable news sources. By cross-referencing advertisement material with verified news articles obtained via various news APIs, the system aims to identify potential misinformation.

# 6. Overview of the code structure
1.	This process involves applying Optical Character Recognition (OCR) technology to analyse images and videos sourced from Facebook advertisements. 
2.	It systematically extracts textual information from these media files and performs. 
3.	Cross-referencing with multiple news API sources. 
4.	This methodology aims to identify potential misinformation by verifying the extracted content against credible news articles.

# 7. Code output 
This program, upon execution, produces a structured output within the IDE terminal across three distinct stages. Initially, it retrieves content items from an SQLite database and incorporates Optical Character Recognition (OCR)-extracted text derived from image files. Subsequently, it performs queries across multiple news APIs, including NewsAPI.org (2019), NewsData (n.d.), WorldNewsAPI (Urbansky, 2022) and TheNewsAPI (2025), to identify articles corresponding to the extracted keywords. During this process, it also displays the queried sources alongside the number of articles retrieved from each. Finally, the program outputs the results divided into two categories: **matched content**, which includes similarity scores, titles, sources, and verification URLs, and **unmatched content**, which highlights items that could not be verified, thereby indicating potential misinformation. Each matched item is accompanied by a confidence percentage (e.g., 20%), whereas unmatched items feature warning indicators. The overall output is designed to facilitate ease of review for manual inspection, detailed analysis, or integration into automated workflows. Additionally, diagnostic messages, such as API errors or file warnings, are provided to assist with troubleshooting during execution.

# 8. Characteristics of the Code

The codebase exhibits a modular architectural design that delineates concerns across various components, including database management, OCR processing, news aggregation, and similarity assessment. Utilising Python's dataclasses, the system enforces type safety within data models, thereby fostering clear and maintainable interfaces between modules. The OCR component employs the Tesseract OCR engine, augmented with preprocessing techniques such as Contrast Limited Adaptive Histogram Equalization (CLAHE) (more information on CLAHE below) and adaptive thresholding, to improve recognition accuracy under conditions of faint or low-contrast text. The news aggregation mechanism integrates multiple sources concurrently, leveraging the parallel querying of diverse news APIs to enhance resilience against rate limiting and service outages. Similarity matching is implemented via Python's `difflib.SequenceMatcher`, facilitating efficient character-based comparisons and subsequent extraction of the most salient keywords, after filtering out common stop words. Metadata associated with media assets and extracted textual content are persistently stored within an SQLite database, enabling comprehensive analysis. The system architecture supports both autonomous scripts (e.g., `database.py`, `facebookAd.py`, `newsAPI.py`) and a consolidated pipeline (`main.py`), thereby providing operational flexibility. Configuration parameters, including thresholds and API credentials, are centralised within the `app/config.py` module, simplifying adjustments and tuning. Overall, the design emphasises extensibility, allowing seamless integration of new APIs, advanced matching algorithms, or enhanced logging frameworks with minimal modifications to existing code. This architectural approach underscores the system’s adaptability and robustness for scalable, maintainable information processing.
## Features of the code
- **Multi-source News Verification**: Supports multiple news APIs (NewsAPI.org, NewsData.io, WorldNewsAPI)
- **OCR Text Extraction**: Uses Tesseract OCR with preprocessing for enhanced text detection
- **Intelligent Matching**: Similarity-based matching between ad content and news articles
- **Database Storage**: SQLite database for storing and managing content
- **Modular Architecture**: Clean separation of concerns with dedicated modules
- **Ad Keyword Detection**: Identifies ads by detecting keywords like "Sponsored" or "Advertisement"

## What is CLAHE? A quick overview
Contrast Limited Adaptive Histogram Equalisation (CLAHE) represents an advanced iteration of Adaptive Histogram Equalisation (AHE), specifically developed to mitigate the risk of over-enhancement in images exhibiting a certain degree of noise (Joseph et al., 2017). Image noise refers to random variations in brightness and colour that manifest as speckles and textures, thereby compromising the clarity and detail of the image, analogous to film grain (Schulz, 2013). The CLAHE algorithm operates by partitioning the image into non-overlapping contextual regions or tiles. Instead of globally adjusting the entire image, the algorithm enhances each individual tile independently before seamlessly blending these enhanced regions to produce a uniformly processed image (Joseph et al., 2017). 



# 9. System Requirements
Note: Commands differ slightly across macOS, Windows, and Linux—follow the OS‑specific steps below.
- **Operating System:** macOS, Linux, or Windows (macOS used for development)
- **Python Version:** 3.8 or higher
- **Tesseract OCR engine:** Install at the OS level (not via pip)
    - macOS: `brew install tesseract`
    - Ubuntu/Debian: `sudo apt-get install tesseract-ocr`
    - Windows: Download from [Tesseract releases](https://github.com/UB-Mannheim/tesseract/wiki) and add to PATH
- **Python Packages:** `pytesseract`, `opencv-python`, `Pillow`, `numpy`, `requests`, `newsapi-python`
    - Install: `pip install -r requirements.txt`
- **Internet Connection:** Required for news API queries
- **API Keys:** Register and configure at least one provider (NewsAPI.org, NewsData.io, WorldNewsAPI; TheNewsAPI optional)
- **Media Folder:** Ensure `image_and_video_directory/` contains files to scan
- **Disk Space:** Sufficient for media files and the SQLite database
- **RAM:** 2GB+ typically sufficient for small images; larger media may require more
Execute all commands from the project root. Verify Tesseract is on your PATH, and confirm installation with `tesseract --version` before running the pipeline.

# 10. Clone repository
You can clone the initial code from the GitHub repository using the following link:
{Link}

# 11. Running the script
- This codebase was developed in Visual Studio Code (VS Code). If you run commands in VS Code, output appears in the integrated terminal.
- Clone or navigate to the project directory.
- Install Tesseract OCR for your OS (see System Requirements above).
- Create and activate a Python virtual environment:
    - macOS/Linux:
        - `python3 -m venv .venv`
        - `source .venv/bin/activate`
    - Windows:
        - `python -m venv .venv`
        - `.venv\Scripts\activate`
- Install Python dependencies:
    - `pip install -r requirements.txt`
- Register at least one news API key (see Prerequisites) and add it to `newsAPI.py`.
- Ensure your media files are in the `image_and_video_directory/` folder.
- Initialize the database and scan files:
    - `python database.py`
- Run the main verification pipeline:
    - `python main.py`
- Optional diagnostics or OCR testing:
    - `python newsAPI.py` (standalone news matching)
    - `python facebookAd.py` (OCR/ad keyword detection)
All output, including results and error messages, will be shown in your terminal. When using VS Code, the integrated terminal provides the best experience.
# 12. Python file and Methods Overview
### `main.py`
The script uses `app.news.fetch_news_articles` to retrieve potentially relevant articles and employs `app.match.match_items_with_news` to identify content-to-article matches. It then presents clear results, such as similarity scores, sources, and URLs. Items lacking matches are marked as potentially unverified. This process integrates configuration settings from `app.config`, data models from `app.models`, and several supporting modules. Use this approach for thorough end-to-end verification of the database content.

### `database.py`
This utility script sets up and populates the `fbContentType.db` Sqlite database with placeholder data and optionally scans media from `image_and_video_directory/`. It handles creating the database schema, inserting records, and scanning directories for images and videos. When processing images, it tries OCR extraction via `FacebookAdScanner.basic_ocr` (from `facebookAd.py`) and saves the text in the `Content_Info` column. The script also displays a formatted table of current records. It is useful for testing and illustrating how OCR-derived text supports downstream matching in `main.py` and `newsAPI.py`.

### `facebookAd.py`
The `FacebookAdScanner` class offers OCR functionality, including a basic OCR method and an improved preprocessing pipeline that involves resizing, converting to grayscale, applying CLAHE, and thresholding to recover faint text using Tesseract with Pillow/OpenCV. When executed directly, it retrieves filenames from the database, resolves them against `image_and_video_directory/`, runs OCR on available images, and heuristically detects ad‑related keywords like “Sponsored”. This module is utilised by `database.py` (to extract text for storage) and `app/ocr.py` (to enhance items dynamically), forming the core OCR component of the project’s verification process flow.

### `newsAPI.py`
This standalone, comprehensive script fetches articles from multiple news sources such as NewsAPI.org, NewsData.io, WorldNewsAPI, and optionally TheNewsAPI. It combines results, calculates basic text similarity using `difflib.SequenceMatcher` between OCR/database content and article titles or descriptions, and outputs relevant articles with their URLs. The script also provides `NEWS_API_SOURCES`, which stores each provider's configuration details, including API keys and whether they are enabled. This setup is imported by the modular `app/news.py` to serve as a unified reference. Use this script for demonstrations, diagnostics, or testing queries and matches outside the main pipeline in `main.py`. 
### `app/config.py`
The central setup for the modular pipeline includes key settings like the database location, scan folder, similarity threshold, language, and page size. These settings are imported by other `app` modules to maintain consistency. The similarity threshold controls how strictly matches are accepted, while language and page size help shape the news API queries. Although API keys are stored separately, it's recommended to centralise all configurations, including secrets, using environment variables in this module for easier management. Any changes here will immediately impact the `app.db`, `app.news`, and `app.match` components, which rely on these settings `main.py`.

### `app/db.py`
The data access layer in the modular architecture manages connections to the SQLite database identified by `app.config.DB_NAME`. It transforms rows from `fbContentType` into `ContentItem` objects stored in `app.models`. This layer offers `fetch_content_items`, which supplies data to `main.py`, and `clear_table` for maintenance or testing. Centralising SQL operations here helps keep other modules database-agnostic. Additionally, this file is the ideal place to add indices, migrations, or extra queries- such as filtering by ad flag or time windows- without needing to change the main pipeline code.

### `app/models.py`
Defines lightweight data models using `dataclasses`: `ContentItem` (a database row with optional `ocr_text`), `NewsArticle` (an abstract view of article fields), and `MatchResult` (associating an item with an article and a similarity score). These models enable consistent data transfer across modules (`app.db`, `app.ocr`, `app.news`, `app.match`, and `main.py`). By centralising this structure, refactoring, typing, and testing are simplified, while keeping presentation or provider-specific details separate from core logic. For stricter validation, upgrading to models like Pydantic is recommended if stricter validation is necessary.

### `app/ocr.py`
The runtime OCR enrichment in the modular pipeline processes a list of `ContentItem`s by attempting to read each file path and, if available, uses `FacebookAdScanner.basic_ocr` (from `facebookAd.py`) to fill in `ocr_text`. This straightforward function allows `main.py` to treat OCR as an optional step, enabling it to continue even if files are missing. It complements `database.py`’s ingestion-time OCR by updating or completing data during analysis without changing the database contents.

### `app/news.py`
A unified interface for querying multiple news providers has been implemented. It defines individual fetchers for providers such as NewsAPI.org, NewsData.io, WorldNewsAPI, and optionally TheNewsAPI, normalising various responses into `NewsArticle` objects and combining the results. The `NEWS_API_SOURCES` from `newsAPI.py` is imported for consistent configuration with the standalone script. The `fetch_news_articles(query)` function is passed to `app.match.match_items_with_news` by `main.py`, clearly separating data retrieval from the matching process. Consider adding caching, retries, or environment‑based keys here to improve resilience and manage quotas efficiently.

### `app/match.py`
Performs keyword extraction and similarity scoring to link database or OCR text with potential news articles. The `extract_keywords` function generates succinct queries by removing common stop words. The `similarity` function employs `SequenceMatcher` to evaluate text similarities, while `match_items_with_news` queries the news API and filters results based on the set similarity threshold (`app.config.SIMILARITY_THRESHOLD`). It produces a list of `MatchResult` objects used by `main.py` for reporting purposes. Since the inputs and outputs are typed (`app.models`), this module is straightforward to test and can be upgraded to incorporate more advanced, semantic matching techniques in the future work.

### `app/__init__.py`
Marks the `app` directory as a Python package, enabling clean module imports like `from app import db, news`. Although currently empty, this file supports the modular architecture used by `main.py`. If you later include package-level helpers or versioning information, this is the right spot. Keeping `__init__.py` simple avoids hidden side effects during imports and facilitates easier unit testing of individual submodules.


## Prerequisites

### Required Software
- **Python 3.8 or higher**
- **Tesseract OCR engine** - Must be installed locally on your system (not a Python package)
- **Virtual environment** (recommended)

### Required API Keys
You **must register** for free API keys from at least one of the following news services:

- **NewsAPI.org**: https://newsapi.org/register (100 requests/day free tier)
- **NewsData.io**: https://newsdata.io/register (500 requests/month free tier)
- **WorldNewsAPI**: https://worldnewsapi.com/register (Free tier available)

**Important**: The system will not function without at least one valid API key configured.

### Installing Tesseract OCR (Required)

Tesseract must be installed **locally on your machine** before running this project. It is **not** a Python package and cannot be installed via pip.

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

**Windows:**
1. Download the installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer and follow the setup wizard
3. Add Tesseract to your system PATH during installation

**Verify Installation:**
```bash
tesseract --version
```
If installed correctly, you should see the Tesseract version information.

## Installation

1. **Clone or navigate to the project directory:**
```bash
cd "../Dissertation Code"
```

2. **Create and activate virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

3. **Install required dependencies:**
```bash
pip install -r requirements.txt
```

4. **Register for News API keys (REQUIRED):**

See Prerequisites → Required API Keys for registration links and free-tier quotas. You must have at least one valid key enabled.

5. **Configure API keys in the project:**

Update your API keys in `newsAPI.py` (line 18-40):
```python
NEWS_API_SOURCES = {
    'newsapi_org': {
        'api_key': 'YOUR_NEWSAPI_ORG_KEY',  # Replace with your actual key
        'enabled': True,  # Set to True to enable this source
    },
    'newsdata_io': {
        'api_key': 'YOUR_NEWSDATA_IO_KEY',  # Replace with your actual key
        'enabled': True,
    },
    'worldnewsapi': {
        'api_key': 'YOUR_WORLDNEWSAPI_KEY',  # Replace with your actual key
        'enabled': True,
    },
}
```

 **Note**: At minimum, enable at least one API source with a valid key. The system aggregates results from all enabled sources.

## Project Structure

```
.
├── app/                          # Modular application package
│   ├── __init__.py
│   ├── config.py                 # Configuration settings
│   ├── db.py                     # Database operations
│   ├── models.py                 # Data models (ContentItem, NewsArticle, MatchResult)
│   ├── ocr.py                    # OCR processing
│   ├── news.py                   # Multi-source news API integration
│   └── match.py                  # Content matching logic
├── database.py                   # Database setup and scanning script
├── facebookAd.py                 # Facebook ad scanner with OCR
├── newsAPI.py                    # News API cross-matching script
├── main.py                       # Main entry point (modular pipeline)
├── image_and_video_directory/   # Directory for media files to analyze
├── fbContentType.db              # SQLite database (created automatically)
└── README.md                     # This file
```

## Usage

### 1. Initialize Database and Scan Files

First, populate the database with media files from the `image_and_video_directory/`:

```bash
python database.py
```

This will:
- Create the `fbContentType.db` SQLite database
- Scan all images and videos in `image_and_video_directory/`
- Extract text using OCR from images
- Store content information in the database

### 2. Run the Main Pipeline

Execute the complete verification pipeline:

```bash
python main.py
```

This will:
- Load all content items from the database
- Perform OCR on image files
- Search for matching news articles across all enabled APIs
- Display matches with similarity scores and URLs
- Flag unmatched content as potential misinformation

### 3. Run News API Matcher (Standalone)

For detailed analysis with the monolithic script:

```bash
python newsAPI.py
```

This provides more verbose output including:
- Detailed similarity scores
- All API sources searched
- Step-by-step matching process

### 4. Scan Individual Files (OCR Testing)

Test OCR on files in the database:

```bash
python facebookAd.py
```

This will:
- Read all files from the database
- Perform OCR with preprocessing
- Detect ad keywords ("Sponsored", "Advertisement")
- Display OCR results for each file

## Understanding the Output

### Matched Content
```
Match #1 | score=20.00%
 - File: hq720.jpg
 - Content: FOX 32 | MAJOR AWS OUTAGE TAKES WEBSITES, APPS OFFLINE
 - Article: Amazon Says AWS Cloud Service is Back to Normal After Outage
 - Source: deccanchronicle
 - URL: https://www.deccanchronicle.com/technology/amazon-says-aws...
```

**Interpretation:** Content was verified against a legitimate news source with 20% similarity.

### Unmatched Content
```
⚠️  File: hello_kitty.jpg
   Content: Hello Kitty is come to town!, Book now for your exclusive offers.
   Status: The information from this post cannot be verified❗️, 
           please be cautious of potential misinformation.
```

**Interpretation:** No matching news articles found - potential false information or promotional content.

## Configuration

### Similarity Threshold

Adjust in `app/config.py`:
```python
SIMILARITY_THRESHOLD = 0.15  # Lower = more matches, higher = stricter matching
```

### News API Sources

Enable/disable sources in `newsAPI.py`:
```python
NEWS_API_SOURCES = {
    'newsapi_org': {
        'api_key': 'YOUR_KEY',
        'enabled': True,  # Set to False to disable
    },
    # ...
}
```

### Database Configuration

Change database name or scan directory in `app/config.py`:
```python
DB_NAME = 'fbContentType.db'
SCAN_DIRECTORY = 'image_and_video_directory'
```


## How It Works

### 1. Content Extraction
```
Image/Video → Tesseract OCR → Text Extraction → Database Storage
```

### 2. Keyword Extraction
```
Content Text → Remove Stop Words → Extract Top 5 Keywords → Search Query
```

### 3. News Matching
```
Search Query → Multi-API Fetch → Similarity Calculation → Match Results
```

### 4. Similarity Scoring
Uses `SequenceMatcher` from Python's `difflib` to calculate text similarity:
- 0.0 = No similarity
- 1.0 = Identical text
- Threshold: 0.15 (configurable)

## Dependencies

Core dependencies (install via requirements.txt):

- `newsapi-python` - NewsAPI.org client
- `requests` - HTTP requests for other APIs
- `pytesseract` - Python wrapper for Tesseract OCR
- `opencv-python` - Image preprocessing
- `Pillow` - Image handling
- `numpy` - Numerical operations

## Troubleshooting

### Tesseract Not Found
```
Error: TesseractNotFoundError
```
**Solution:** Install Tesseract OCR and ensure it's in your PATH.

### API Rate Limit Exceeded
```
⚠️ NewsAPI.org error: rateLimited
```
**Solution:** Wait 24 hours for quota reset or enable other API sources.

### No Matches Found
```
Found 0 matches
```
**Possible causes:**
- Similarity threshold too high (try lowering to 0.10-0.15)
- API quota exhausted (check enabled sources)
- Content is truly unverified (potential misinformation)

### File Not Found Errors
```
⚠️ File not found: image.jpg
```
**Solution:** Ensure files are in `image_and_video_directory/` or database contains full paths.

---
# 14. Reference:

Bakir, V. (2020). Psychological Operations in Digital Political Campaigns: Assessing Cambridge Analytica’s Psychographic Profiling and Targeting. *Frontiers in Communication*, [online] 5. doi: [https://doi.org/10.3389/fcomm.2020.00067](https://doi.org/10.3389/fcomm.2020.00067) [Accessed 9 Oct. 2025].

BBC Bitesize (2024). *Timeline of how online misinformation fuelled UK riots - BBC Bitesize*. [online] BBC Bitesize. Available at: [https://www.bbc.co.uk/bitesize/articles/zshjs82](https://www.bbc.co.uk/bitesize/articles/zshjs82) [Accessed 9 Oct. 2025].

BBC News (2018b). The global reach of Cambridge Analytica. *BBC News*. [online] 22 Mar. Available at: [https://www.bbc.com/news/world-43476762](https://www.bbc.com/news/world-43476762) [Accessed 14 Oct. 2025].

Benesch, S. (2021). *Nobody Can See Into Facebook*. [online] Available at: [http://www.businessforum.com/Atlantic_10-30-2021.pdf](http://www.businessforum.com/Atlantic_10-30-2021.pdf) [Accessed 11 Aug. 2025].

Byte Myke (2021). *SQLite beginner crash course in Visual Studio Code - 2022*. [online] YouTube. Available at: [https://www.youtube.com/watch?v=IBgWKTaG_Bs](https://www.youtube.com/watch?v=IBgWKTaG_Bs) [Accessed 19 Oct. 2025].

Dam, V.H., Hjordt, L.V., Cunha‐Bang, S., Sestoft, D., Knudsen, G.M. and Stenbæk, D.S. (2021). Trait aggression is associated with five‐factor personality traits in males. *Brain and Behavior*, [online] 11(7). doi: [https://doi.org/10.1002/brb3.2175](https://doi.org/10.1002/brb3.2175) [Accessed 3 Oct. 2025].

Dixon, S.J. (2025c). *Most Popular Social Networks Worldwide as of February 2025, by Number of Monthly Active Users*. [online] Statista. Available at: [https://www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-users/](https://www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-users/) [Accessed 4 Aug. 2025].

free-news-api (2024). *GitHub - free-news-api/news-api: Top Free News API Comparison*. [online] GitHub. Available at: [https://github.com/free-news-api/news-api](https://github.com/free-news-api/news-api) [Accessed 18 Oct. 2025].

Fung, B. (2024). *UK riots show how social media can fuel real-life harm. It’s only getting worse*. [online] CNN. Available at: [https://edition.cnn.com/2024/08/09/tech/uk-protests-social-media](https://edition.cnn.com/2024/08/09/tech/uk-protests-social-media) [Accessed 9 Oct. 2025].

GeeksforGeeks (2024). *Introduction to Python Pytesseract Package*. [online] GeeksforGeeks. Available at: [https://www.geeksforgeeks.org/python/introduction-to-python-pytesseract-package/](https://www.geeksforgeeks.org/python/introduction-to-python-pytesseract-package/) [Accessed 18 Oct. 2025].

History.com Editors (2018). *The 2016 U.S. Presidential Election*. [online] HISTORY. Available at: [https://www.history.com/articles/us-presidential-election-2016](https://www.history.com/articles/us-presidential-election-2016) [Accessed 3 Sep. 2025].

Joseph, J., Sivaraman, J., Periyasamy, R. and Simi, V.R. (2017). An objective method to identify optimum clip-limit and histogram specification of contrast limited adaptive histogram equalization for MR images. *Biocybernetics and Biomedical Engineering*, 37(3), pp.489–497. doi: [https://doi.org/10.1016/j.bbe.2016.11.006](https://doi.org/10.1016/j.bbe.2016.11.006) [Accessed 19 Oct. 2025].

Kiderlin, S. (2024). *Online disinformation sparked a wave of far-right violence in the UK — here’s how*. [online] CNBC. Available at: [https://www.cnbc.com/2024/08/09/online-disinformation-sparked-a-wave-of-far-right-violence-in-the-uk.html](https://www.cnbc.com/2024/08/09/online-disinformation-sparked-a-wave-of-far-right-violence-in-the-uk.html) [Accessed 9 Oct. 2025].

Kite (2000). *Sqlite 3 Python Tutorial in 5 minutes - Creating Database, Tables and Querying [2020] *. [online] www.youtube.com. Available at: [https://www.youtube.com/watch?v=girsuXz0yA8](https://www.youtube.com/watch?v=girsuXz0yA8) [Accessed 18 Oct. 2025].

Lee, M. (2022). *pytesseract: Python-tesseract is a python wrapper for Google’s Tesseract-OCR*. [online] PyPI. Available at: [https://pypi.org/project/pytesseract/](https://pypi.org/project/pytesseract/) [Accessed 18 Oct. 2025].

Legislation.Gov.UK (2023). *Online Safety Act 2023*. [online] Legislation.gov.uk. Available at: [https://www.legislation.gov.uk/ukpga/2023/50](https://www.legislation.gov.uk/ukpga/2023/50) [Accessed 9 Oct. 2025].

Lim, A. (2025). Big Five Personality Traits: The 5-Factor Model Of Personality. *Simply Psychology*. [online] Available at: [https://www.simplypsychology.org/big-five-personality.html](https://www.simplypsychology.org/big-five-personality.html) [Accessed 1 Oct. 2025].

mattlisiv (2018). *GitHub - mattlisiv/newsapi-python: A Python Client for News API*. [online] GitHub. Available at: [https://github.com/mattlisiv/newsapi-python](https://github.com/mattlisiv/newsapi-python) [Accessed 19 Oct. 2025].

Meta (2022). *Facebook Data policy*. [online] Facebook. Available at: [https://www.facebook.com/about/privacy/update/printable](https://www.facebook.com/about/privacy/update/printable) [Accessed 31 Aug. 2025].

Mohamed, E. (2024). *Southport stabbing: What led to the spread of disinformation? * [online] Al Jazeera. Available at: [https://www.aljazeera.com/news/2024/8/2/southport-stabbing-what-led-to-the-spread-of-disinformation](https://www.aljazeera.com/news/2024/8/2/southport-stabbing-what-led-to-the-spread-of-disinformation) [Accessed 9 Oct. 2025].

Netflix (2019). *The Great Hack | Netflix Official Site*. [online] www.netflix.com. Available at: [https://www.netflix.com/gb/title/80117542](https://www.netflix.com/gb/title/80117542) [Accessed 8 Sep. 2025].

Newsapi.org (2019). *News API - A JSON API for live news and blog articles*. [online] Newsapi.org. Available at: [https://newsapi.org/](https://newsapi.org/) [Accessed 19 Oct. 2025].

NewsData (n.d.). *NewsData - News API to Search & Collect Worldwide News*. [online] Newsdata. Available at: [https://newsdata.io/](https://newsdata.io/) [Accessed 19 Oct. 2025].

NumPy (2022). *NumPy Documentation*. [online] numpy.org. Available at: [https://numpy.org/doc/](https://numpy.org/doc/) [Accessed 19 Oct. 2025].

Nyabola, N. (2019). *The spectre of Cambridge Analytica still haunts African elections*. [online] Al Jazeera. Available at: [https://www.aljazeera.com/opinions/2019/2/15/the-spectre-of-cambridge-analytica-still-haunts-african-elections](https://www.aljazeera.com/opinions/2019/2/15/the-spectre-of-cambridge-analytica-still-haunts-african-elections) [Accessed 14 Oct. 2025].

Opencv.org (n.d.). *OpenCV documentation index*. [online] docs.opencv.org. Available at: [https://docs.opencv.org/](https://docs.opencv.org/) [Accessed 19 Oct. 2025].

Pillow.readthedocs.io (n.d.). *Pillow — Pillow (PIL Fork) 7.2.0 documentation*. [online] pillow.readthedocs.io. Available at: [https://pillow.readthedocs.io/](https://pillow.readthedocs.io/) [Accessed 19 Oct. 2025].

Prichard, E.C. (2021). Is the Use of Personality Based Psychometrics by Cambridge Analytical Psychological Science’s ‘Nuclear Bomb’ Moment?. *Frontiers in Psychology*, [online] 12. doi: [https://doi.org/10.3389/fpsyg.2021.581448](https://doi.org/10.3389/fpsyg.2021.581448) [Accessed 14 Sep. 2025].

PyPi (2019). *opencv-python*. [online] PyPI. Available at: [https://pypi.org/project/opencv-python/](https://pypi.org/project/opencv-python/) [Accessed 18 Oct. 2025].

Python Software Foundation (2024). *sqlite3 — DB-API 2.0 interface for SQLite databases — Python 3.8.2 documentation*. [online] docs.python.org. Available at: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)  [Accessed 19 Oct. 2025].

Python.org (n.d.). *difflib — Helpers for computing deltas*. [online] Python documentation. Available at: [https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher) [Accessed 19 Oct. 2025].

Renotte, N. (2021). *How to Install OpenCV for Python // OpenCV for Beginners*. [online] YouTube. Available at: [https://www.youtube.com/watch?v=M6jukmppMqU](https://www.youtube.com/watch?v=M6jukmppMqU) [Accessed 18 Oct. 2025].

Requests.readthedocs.io (n.d.). *Requests: HTTP for HumansTM — Requests 2.31.0 documentation*. [online] requests.readthedocs.io. Available at: [https://requests.readthedocs.io/](https://requests.readthedocs.io/) [Accessed 19 Oct. 2025].

SBS News (2018). *‘Likely’ Australians caught up in Cambridge Analytica data scandal*. [online] SBS News. Available at: [https://www.sbs.com.au/news/article/likely-australians-caught-up-in-cambridge-analytica-data-scandal/bnh3h7olz](https://www.sbs.com.au/news/article/likely-australians-caught-up-in-cambridge-analytica-data-scandal/bnh3h7olz) [Accessed 14 Oct. 2025].

Schulz, J. (2013). Geometric optics and strategies for subsea imaging. [online] doi: [https://doi.org/10.1533/9780857093523.3.243](https://doi.org/10.1533/9780857093523.3.243) [Accessed 19 Oct. 2025].

Shah, M. (2024). *Fanning the Flames: Online Misinformation and Far-Right Violence in the UK - GNET*. [online] GNET. Available at: [https://gnet-research.org/2024/08/28/fanning-the-flames-online-misinformation-and-far-right-violence-in-the-uk/](https://gnet-research.org/2024/08/28/fanning-the-flames-online-misinformation-and-far-right-violence-in-the-uk/) [Accessed 9 Oct. 2025].

Socratica (2023). *SQLite in Python || Python Tutorial || Learn Python Programming*. [online] www.youtube.com. Available at: [https://www.youtube.com/watch?v=c8yHTlrs9EA](https://www.youtube.com/watch?v=c8yHTlrs9EA) [Accessed 18 Oct. 2025].

SQLite (2014). *Datatypes In SQLite Version 3*. [online] Sqlite.org. Available at: [https://www.sqlite.org/datatype3.html](https://www.sqlite.org/datatype3.html)  [Accessed 19 Oct. 2025].

Sutton, J. (2025). *Big Five Personality Traits: The OCEAN Model Explained [2019 Upd.] *. [online] PositivePsychology.com. Available at: [https://positivepsychology.com/big-five-personality-theory/](https://positivepsychology.com/big-five-personality-theory/) [Accessed 2 Oct. 2025].

Tesseract-ocr.github (2020). *Tesseract User Manual*. [online] tessdoc. Available at: [https://tesseract-ocr.github.io/tessdoc/](https://tesseract-ocr.github.io/tessdoc/)  [Accessed 19 Oct. 2025].

The New York Times (2017). Presidential Election Results: Donald J. Trump Wins. *The New York Times*. [online] 9 Aug. Available at: [https://www.nytimes.com/elections/2016/results/president](https://www.nytimes.com/elections/2016/results/president) [Accessed 3 Sep. 2025].

The News API (2025). *Free live and top story JSON news API | The News API*. [online] Thenewsapi.com. Available at: [https://www.thenewsapi.com/](https://www.thenewsapi.com/) [Accessed 19 Oct. 2025].

Urbansky, D. (2022). *World News API. * [online] Worldnewsapi.com. Available at: [https://worldnewsapi.com/](https://worldnewsapi.com/) [Accessed 19 Oct. 2025].

Woods, L. (2024). *Disinformation and disorder: the limits of the Online Safety Act. * [online] Online Safety Act Network. Available at: [https://www.onlinesafetyact.net/analysis/disinformation-and-disorder-the-limits-of-the-online-safety-act/](https://www.onlinesafetyact.net/analysis/disinformation-and-disorder-the-limits-of-the-online-safety-act/) [Accessed 9 Oct. 2025].

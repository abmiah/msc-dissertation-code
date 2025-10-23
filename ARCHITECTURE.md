# Restructured Code Architecture

# 1. Introduction
This document outlines the architecture of the Facebook Ad Content Verification System, a Python-based computational framework designed to identify and authenticate misinformation in social media advertisements. The system employs Optical Character Recognition (OCR) technology to extract textual data from images and videos, then stores this information in a structured SQLite database. It performs content comparison against multiple reputable news APIs, including NewsAPI.org, NewsData.io, WorldNewsAPI, and optionally, TheNewsAPI. By calculating similarity metrics between advertisement content and verified journalistic sources, the system facilitates the detection of potentially false or unverified information. The architectural design was refactored from a monolithic script to a modular structure, delineating distinct components including database management, OCR processing, news collection, and content matching. This modularity enhances the system’s flexibility, supporting both standalone diagnostic scripts and integrated pipelines, thereby catering to research, testing, and automation needs. Emphasising extensibility, testability, and configurability, the system serves as a valuable tool for academic research, policy development, and cybersecurity initiatives to combat digital misinformation.

# 2. Overview
The codebase has undergone systematic restructuring to adopt a modular architecture, thereby enhancing maintainability and facilitating rigorous testing. Each module within the `app/` directory is dedicated to a specific function: `config.py` manages configuration settings, including database paths, API keys, similarity thresholds, and language options; `models.py` defines standardized data structures utilising Python dataclasses such as `ContentItem`, `NewsArticle`, and `MatchResult`; `db.py` oversees SQLite database operations, encompassing data retrieval and table management; `ocr.py` employs the `FacebookAdScanner` class to incorporate OCR-extracted text into content items; `news.py` aggregates news articles from diverse APIs and standardizes the response formats; and `match.py` performs keyword extraction, similarity scoring, and content-to-article matching. The `main.py` script orchestrates these modules to execute the comprehensive verification pipeline—spanning database extraction, OCR enrichment, news collection, similarity analysis, and result presentation. Legacy scripts, including `database.py`, `facebookAd.py`, and `newsAPI.py`, remain available to ensure backward compatibility and diagnostic functionality, enabling isolated execution of individual components outside the primary workflow. This modular configuration fosters independent testing, component reuse, and component replacement with minimal systemic disruption.

## Structure

```
app/
├── __init__.py
├── config.py       # All configuration (DB path, API keys, thresholds)
├── models.py       # Data models (ContentItem, NewsArticle, MatchResult)
├── db.py           # Database operations (fetch, clear)
├── ocr.py          # OCR wrapper (enrich items with FacebookAdScanner)
├── news.py         # News API client (fetch articles)
└── match.py        # Matching logic (similarity scoring, keyword extraction)

main.py             # CLI entry point: run the full pipeline
database.py         # Original DB setup script (still works)
facebookAd.py       # Original OCR/ad scanner (reused by app/)
newsAPI.py          # Original news matcher (can still be used standalone)
```

# 3. Usage

## Running the System
This codebase has been developed utilizing the Visual Studio Code (VS Code) environment. For optimal performance, it is strongly recommended to utilize VS Code. All outputs are configured to be displayed within the integrated terminal upon execution of the commands outlined below. To execute the comprehensive verification procedure, users should run the `main.py` script, which orchestrates all essential steps: retrieving content from the database, incorporating OCR-extracted text into items, querying various news APIs, and calculating similarity metrics. Simply run:
```bash
python main.py
```
This command outputs results within the terminal environment, presenting matched content accompanied by similarity scores, article titles, sources, and URLs. It also displays unmatched content, which is flagged as potentially unverified or indicative of misinformation. For purposes of diagnostic evaluation or individual component testing, the original scripts remain accessible. Specifically, executing `python database.py` performs a scan of media files to populate the SQLite database with placeholder data and OCR-extracted text; `python facebookAd.py` conducts optical character recognition on images to detect ad-related keywords such as "Sponsored'; and `python newsAPI.py` compares database entries with news articles, providing detailed similarity scores along with source information. Prior to executing any script, it is recommended to activate your virtual environment using `source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\\activate` on Windows. Additionally, ensure dependencies are installed via `pip install -r requirements.txt`, configure at least one news API key within the `newsAPI.py` script, and place media files into the designated `image_and_video_directory/` folder. All output, including diagnostic messages and errors, will be displayed in the terminal for comprehensive review.

## Key Benefits
- **Separation of concerns**: Each module has one job
- **Testable**: Pure functions, easy to unit-test
- **Reusable**: Modules can be imported independently
- **Type hints**: Better IDE support and fewer bugs
- **Config management**: Single source of truth for settings
- **Dataclasses**: Clean data models vs raw tuples

## Next Steps (Optional)
- Add CLI args (e.g., `python main.py --threshold 0.3`)
- Add logging (structured logs for debugging)
- Add tests (`tests/test_match.py`, etc.)
- Add `requirements.txt` or `pyproject.toml`
- Add subcommands (`main.py scan`, `main.py match`, `main.py reset`)

---

# 3. Summary
This architectural framework represents a comprehensive reengineering of the Facebook Advertisement Content Verification System, transitioning from a monolithic, script-driven architecture to a modular and maintainable Python-based application. It exemplifies the integration of optical character recognition (OCR), multi-source news aggregation, and similarity-based content matching techniques to effectively identify potential misinformation in social media advertisements. The system architecture delineates responsibilities across specialized modules (e.g., `config`, `models`, `db`, `ocr`, `news`, `match`), promoting individual testability, reusability, and ease of extension. Employing Python dataclasses facilitates type-safe data modeling, while centralized configuration management and an orchestration layer (`main.py`) form a robust foundation suitable for applications in academia, policy development, and cybersecurity. The retention of legacy scripts ensures backward compatibility and diagnostic capabilities, allowing for targeted execution and troubleshooting of specific components. Emphasizing clarity, scalability, and fault tolerance, the design supports seamless integration of additional functionalities such as new APIs, advanced semantic similarity matching techniques, enhanced logging, and monitoring systems. This modular architecture not only addresses current requirements but also provides a scalable platform for future enhancements, including command-line interface (CLI) argument parsing, comprehensive unit testing, API caching strategies, and web-based or automated misinformation detection systems.

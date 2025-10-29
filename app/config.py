""" 
The app/config.py module outlines the application's configuration constants, including the database name, 
scan directory, news API key, similarity threshold, page size, and language settings. These constants are 
used consistently throughout the application to maintain uniform configuration values.

The variables defined in this module include:
- DB_NAME: The name of the SQLite database file.
- SCAN_DIRECTORY: The directory path where images and videos are scanned.
- NEWS_API_KEY: The API key used for accessing news services.
- SIMILARITY_THRESHOLD: The threshold value for determining similarity in matching.
- PAGE_SIZE: The number of items to fetch per page from news APIs.
- LANGUAGE: The language setting for content retrieval.
"""

DB_NAME = 'fbContentType.db'
SCAN_DIRECTORY = 'image_and_video_directory'
NEWS_API_KEY = '7db691a7480b4488b8c544b417996e8a'
SIMILARITY_THRESHOLD = 0.15
PAGE_SIZE = 20
LANGUAGE = 'en'
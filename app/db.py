""" 
The `app/db.py` module contains functions for interacting with an SQLite database, specifically for retrieving 
content items and clearing the content table. It starts by importing the `sqlite3` library, which is used for 
database operations, as well as the `ContentItem` model that represents individual content items.

This module defines functions to establish a database connection, fetch content items from the `fbContentType` 
table, and delete all entries from that table. Each function is designed to perform database operations in a clear 
and straightforward manner, allowing the application to efficiently access and manage the content item data stored 
in the SQLite database.
"""

import sqlite3
from typing import List
from .models import ContentItem
from .config import DB_NAME


""" 
The function get_db_connection creates a connection to the SQLite database using the specified database path, 
defaulting to DB_NAME as indicated in the configuration. It returns a connection object for database interaction.
"""
def get_db_connection(db_path: str = DB_NAME):
    return sqlite3.connect(db_path)


""" 
The `fetch_content_items` function retrieves all content items from the `fbContentType` table in the SQLite database. 
It establishes a connection to the database, executes a SQL query to select the relevant fields, and then creates a 
list of `ContentItem` objects based on the retrieved rows.
"""
def fetch_content_items() -> List[ContentItem]:
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute(
            """
            SELECT File_Name, Content_Info, Locations, Facebook_Ad, User_Content
            FROM fbContentType
            """
        )
        rows = c.fetchall()
        items: List[ContentItem] = []
        for file_name, content_info, location, facebook_ad, user_content in rows:
            items.append(
                ContentItem(
                    file_name=file_name,
                    content_info=content_info or "",
                    location=location or "",
                    is_facebook_ad=bool(facebook_ad),
                    is_user_content=bool(user_content),
                )
            )
        return items


""" 
The clear_table function removes all entries from the fbContentType table in the SQLite database. 
It creates a connection, executes a SQL DELETE command, and commits the changes.
"""
def clear_table():
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM fbContentType")
        conn.commit()

        
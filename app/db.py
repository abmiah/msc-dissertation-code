""" The app/db.py module provides functions to interact with the SQLite database,
specifically for fetching content items and clearing the content table. It begins by importing
the sqlite3 library for database operations and the ContentItem model for representing content items.
The module defines a function to establish a database connection, fetch content items from the
fbContentType table, and clear all entries from that table. Each function is designed to handle
database operations in a straightforward manner, ensuring that the application can easily retrieve
and manage content item data stored in the SQLite database."""

import sqlite3
from typing import List
from .models import ContentItem
from .config import DB_NAME


""" The initial function get_db_connection establishes a connection to the SQLite database
using the provided database path (defaulting to DB_NAME from the config). It returns a connection
object that can be used to interact with the database. """
def get_db_connection(db_path: str = DB_NAME):
    return sqlite3.connect(db_path)


""" The fetch_content_items function retrieves all content items from the fbContentType table
in the SQLite database. It establishes a database connection, executes a SQL query to select
the relevant fields, and constructs a list of ContentItem objects from the fetched rows."""
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


""" The last function clear_table removes all entries from the fbContentType table in the SQLite database.
It establishes a database connection, executes a SQL DELETE command, and commits the changes to the database."""
def clear_table():
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM fbContentType")
        conn.commit()

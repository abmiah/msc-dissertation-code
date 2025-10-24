""" 
This module provides functionality to enrich content items with OCR text extracted from image files. 
It begains by importing necessary libraries and the ContentItem model. The os module is used to check for file existence,
and the List type from typing is used for type hinting. The enrich_with_ocr function iterates through a list of ContentItem objects,
checks if the associated file exists, and if so, uses the FacebookAdScanner class to perform OCR on the image file.
The extracted text is then assigned to the ocr_text attribute of the ContentItem. If any exception occurs during this process,
the ocr_text attribute is set to None.

"""

import os
from typing import List
from .models import ContentItem
from facebookAd import FacebookAdScanner


""" This single function enriches a list of ContentItem objects with OCR text extracted from their associated image files.
Within the function is has an if statement to check if the file exists before attempting OCR. Also an try-except block is used
to handle any exceptions that may occur during the OCR process, ensuring that the program continues to run smoothly even if some files cannot be processed.
"""
def enrich_with_ocr(items: List[ContentItem]) -> List[ContentItem]:
    """Enriches a list of ContentItem objects with OCR text extracted from their associated image files."""
    scanner = FacebookAdScanner()
    for item in items:
        try:
            if item.file_name and os.path.exists(item.file_name):
                item.ocr_text = scanner.basic_ocr(item.file_name)
        except Exception:
            item.ocr_text = None
    return items
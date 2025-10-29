""" 
This module provides functionality to enhance content items by extracting text from image files 
using optical character recognition (OCR). It begins by importing the necessary libraries and the 
`ContentItem` model. The `os` module is used to check whether a file exists, and the `List` type 
from the `typing` module is employed for type hinting.

The `enrich_with_ocr` function processes a list of `ContentItem` objects. For each item, it checks 
if the associated file exists. If the file is present, the function utilizes the `FacebookAdScanner` 
class to perform OCR on the image file. The extracted text is then assigned to the `ocr_text` 
attribute of the `ContentItem`. If any exceptions occur during this process, the `ocr_text` attribute 
is set to `None`.

"""

import os
from typing import List
from .models import ContentItem
from facebookAd import FacebookAdScanner


""" 
This function enhances a list of ContentItem objects by extracting OCR (Optical Character Recognition) 
text from their associated image files. It includes a conditional statement to check if the file exists 
before attempting to perform OCR. Additionally, a try-except block is used to handle any exceptions that 
may occur during the OCR process, ensuring that the program runs smoothly even if some files cannot be processed.
"""
def enrich_with_ocr(items: List[ContentItem]) -> List[ContentItem]:
    """ Enriches a list of ContentItem objects with OCR text extracted from their associated image files. """
    scanner = FacebookAdScanner()
    for item in items:
        try:
            if item.file_name and os.path.exists(item.file_name):
                item.ocr_text = scanner.basic_ocr(item.file_name)
        except Exception:
            item.ocr_text = None
    return items
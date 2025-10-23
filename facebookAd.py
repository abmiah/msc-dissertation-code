""" 
This section of code is designed to scan a Facebook user domain to identify any advertisements. If advertisements are found, 
the details will be retrieved and stored in the 'fbContentType.db' database for further analysis. Since this is a hypothetical 
example, the actual process of scanning Facebook for ads is not included. Instead, the code will search the local file system of 
this project for demo media to simulate the presence of ads and run OCR on the image using Tesseract if available.

Note: pytesseract is a wrapper around the native 'tesseract' binary. One must have the 'tesseract' executable installed and
available on PATH for OCR to work.
"""

""" Import necessary libraries to handle file operations and database interactions. """
import os
import cv2
from PIL import Image
import pytesseract
import numpy as np

""" 
This class will first scan the ads in the facebook user domain. If ads are found, it will store the details in the database.
Because this is a hypothetical example, the actual scanning process is not implemented. Instead, it will look for specific files in the
local file system within the 'image_and_video_directory/'. The information on the ad will be stored in the 'fbContentType.db' database.
"""
class FacebookAdScanner:
    def __init__(self, ad_keywords=None):
        """ 
        First we need to check for 'Advertisement' or 'Sponsored' keywords in the text extracted from images. 
        This will identify if the content is an ad.
        """
        if ad_keywords is None:
            ad_keywords = ["Advertisement", "Sponsored"]
        self.ad_keywords = ad_keywords

    def contains_ad_keywords(self, text):
        """
        Checks if the text contains advertising-related keywords. 
        Returns (True, matched_keyword) if any keyword is found, False otherwise.
        """
        text_lower = text.lower()
        for keyword in self.ad_keywords:
            keyword_lower = keyword.lower()
            if keyword_lower in text_lower:
                """ The import re statement is used here to perform case-insensitive matching of the keyword in the text. """
                import re
                match = re.search(keyword, text, re.IGNORECASE)
                if match:
                    return (True, match.group(0))
                else:
                    return (True, keyword)
        return False

    def ocr_with_preprocessing(self, image_path, upscale_fx=2, upscale_fy=2):
        """
        Performs OCR with preprocessing for enhanced faint text recovery.
        Returns a list with results from both normal and inverted contrast.
        """
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Could not open or find image: {image_path}")

        # Optionally upscale to help OCR
        """ This section upscales the image to improve OCR accuracy. 
        As the image resolution increases, the OCR engine can better recognise faint text. 
        """
        img = cv2.resize(img, (0, 0), fx=upscale_fx, fy=upscale_fy)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        results = []
        for processed in [gray, cv2.bitwise_not(gray)]:
            # Enhance contrast using CLAHE
            clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8,8))
            enhanced = clahe.apply(processed)
            # Adaptive thresholding
            adaptive = cv2.adaptiveThreshold(
                enhanced, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 10)
            text = pytesseract.image_to_string(Image.fromarray(adaptive))
            results.append(text)
        return results

    """ This function performs the basic OCR on the original image without preprocessing. """
    def basic_ocr(self, filepath):
        image = Image.open(filepath)
        return pytesseract.image_to_string(image)
    
""" If run as main, demonstrate the OCR and ad keyword detection. """
if __name__ == "__main__":
    scanner = FacebookAdScanner()
    filepath = "/Users/amrol/Desktop/MSc Cyber Security/10. Dissertation/Dissertation Code/image_and_video_directory/hq720.jpg"
    ocr_results = scanner.ocr_with_preprocessing(filepath)
    for i, text in enumerate(ocr_results):
        print(f"----- Preprocessing Version {i+1} -----\n{text}")
        result = scanner.contains_ad_keywords(text)
        print(f"Contains ad keywords: {result}\n")
        if result and result[0]:
            print("Ad keyword detected: Needs to be verified!\n")
    # Vanilla OCR baseline
    basic_text = scanner.basic_ocr(filepath)
    print("----- Basic OCR result -----")
    print(basic_text)
    print(f"Contains ad keywords: {scanner.contains_ad_keywords(basic_text)}")

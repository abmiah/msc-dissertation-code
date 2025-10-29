""" 
This section of code is intended to scan a Facebook user's domain for advertisements. 
If advertisements are detected, their details will be retrieved and stored in a database named 
'fbContentType.db' for further analysis. Since this is a hypothetical example, the actual process 
of scanning Facebook for ads is not included. Instead, the code will search the local file system 
of this project for files named 'image_by_jon_smith.jpg' or 'video_by_jane_doe.mp4' to simulate 
the presence of ads.
"""
import sqlite3
import os
from pathlib import Path
from facebookAd import FacebookAdScanner


# Column widths for table display
# The widths are slightly adjusted here for better accommodation of headers
""" 
The widths of the columns for the database table display are defined in the COLUMN_WIDTHS list. 
This allows for better formatting of the output table, with each width corresponding to a specific 
column in the fbContentType database table.
"""
COLUMN_WIDTHS = [10, 20, 12, 12, 9, 9, 9, 12, 40]

# Directory to scan for image and video files
""" 
The SCAN_DIRECTORY constant specifies the directory to scan for image and video files. 
For this coding project, the directory is named 'image_and_video_directory/'. 
This directory is stored locally within the project structure.
"""
SCAN_DIRECTORY = 'image_and_video_directory'

# Placeholder sample data - for demonstration and testing purposes
""" 
This list contains sample records to be inserted into the fbContentType database table. 
Each entry represents a record with fields such as file type, file name, ad flags, engagement 
metrics, location, and content information.
"""

""" 
The database structure is as follows, which can be seen in the def create_facebook_ads_table() function:
    - File_Type: Type of the file (image or video)
    - File_Name: Name of the file
    - Facebook_Ad: Boolean flag indicating if it's a Facebook ad
    - User_Content: Boolean flag indicating if it's user-generated content
    - No_Shares: Number of shares
    - No_Comments: Number of comments
    - No_Likes: Number of likes
    - Locations: Location information
    - Content_Info: Extracted content information from OCR or metadata
"""
PLACEHOLDER_DATA = [
    (
        'image',
        'hello_kitty.jpg',
        1, 0, 500, 85, 1200,
        'London, UK',
        'Hello Kitty is come to town!, Book now for your exclusive offers.'
    ),
    (
        'video',
        'hello_kitty_video.mp4',
        1, 0, 500, 85, 1200,
        'London, UK',
        'Hello Kitty - LIVE!, Book now for your exclusive offer, limited time only.'
    ), 
    (
        'image',
        'david_image_labour.png',
        0, 1, 10, 5, 0,
        'Manchester, UK',
        'Labour Government does not like cats. Evidence shows that David is a Parrot lover.'
    )
]


""" This function establishes a connection to the SQLite database specified by db_path. """
def get_db_connection(db_path=':memory:'):
    """Establishes a connection to the SQLite database specified by db_path."""
    return sqlite3.connect(db_path)


""" This function creates the fbContentType table in the database if it does not already exist. """
def create_facebook_ads_table(cursor):
    """Creates the fbContentType table in the database if it does not already exist."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fbContentType (
            File_Type TEXT NOT NULL,
            File_Name TEXT NOT NULL,
            Facebook_Ad BOOLEAN DEFAULT 0,
            User_Content BOOLEAN DEFAULT 0,
            No_Shares INTEGER DEFAULT 0,
            No_Comments INTEGER DEFAULT 0,
            No_Likes INTEGER DEFAULT 0,
            Locations TEXT,
            Content_Info TEXT,
            Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')


def clear_table(cursor):
    """ Clears all records from the fbContentType table. """
    cursor.execute('DELETE FROM fbContentType')


""" This function inserts multiple records into the fbContentType table using executemany for efficiency. """
def insert_multiple_fb_content_types(cursor, content_data_list):
    """ Inserts multiple records into the fbContentType table using executemany for efficiency. """
    cursor.executemany('''
        INSERT INTO fbContentType (
            File_Type, File_Name, Facebook_Ad, User_Content,
            No_Shares, No_Comments, No_Likes, Locations, Content_Info
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', content_data_list)


""" This function formats a row of data for table display, centering each item within its column width."""
def format_row(data, widths):
    """
    Format a row of data with centered alignment and fixed widths.
    Truncates long data and adds an ellipsis for readability.
    """
    is_header = all(isinstance(item, str) for item in data)
    formatted_data = []
    
    for item, width in zip(data, widths):
        item_str = str(item)
        # Truncate if not a header AND the string is longer than the column width
        display_str = item_str if (is_header or len(item_str) <= width) else item_str[:width - 3] + '...'
        formatted_data.append(f"{display_str:^{width}}")
    
    return '|' + '|'.join(formatted_data) + '|'


""" This function prints the contents of the fbContentType table in a formatted table layout. """
def print_table(cursor):
    """ Print database contents in a formatted table. """
    cursor.execute('SELECT * FROM fbContentType')
    all_rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    
    print("\n--- Database Content Table ---")
    header_row = format_row(column_names, COLUMN_WIDTHS)
    separator = '-' * len(header_row)
    
    print(f"{separator}\n{header_row}\n{separator}")
    for row in all_rows:
        print(f"{format_row(row, COLUMN_WIDTHS)}\n{separator}")


def scan_files_for_ads(directory):
    """
   The program scans a specified directory for image and video files. It uses Optical Character Recognition (OCR) 
   to extract text from these images and stores the extracted information in a variable called Content_Info. 
   Additionally, it determines whether the files are advertisements based on filename patterns, specifically looking 
   for the presence of the word "ad" or certain keywords. Finally, the program returns a list of tuples that are 
   formatted for database insertion.
    """
    if not os.path.exists(directory):
        print(f"Warning: Directory '{directory}' not found. Creating it...")
        os.makedirs(directory, exist_ok=True)
        return []
    
    # Initialize OCR scanner
    scanner = FacebookAdScanner()
    
    # Media file extensions
    """ 
    The media_extensions dictionary defines the file extensions for images and videos. 
    This helps in identifying the type of media file during the scanning process. 
    """
    media_extensions = {
        'image': {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'},
        'video': {'.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv'}
    }
    
    """ 
    The `content_data` list is initially empty and will store the tuples of data that need to be inserted into the database. 
        Each tuple corresponds to a media file found in the specified directory, along with its associated information.

    The function processes each file in the directory, checking its extension to determine if it's an image or a video. 
    For images, it performs Optical Character Recognition (OCR) to extract text. Additionally, it identifies whether the file 
    is an advertisement based on its filename and adds the relevant data to the `content_data` list.
    """
    content_data = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            continue
        
        file_ext = Path(filename).suffix.lower()
        
        # Determine file type
        file_type = None
        for media_type, extensions in media_extensions.items():
            if file_ext in extensions:
                file_type = media_type
                break
        
        if not file_type:
            continue
        
        # Extract OCR text from images
        content_info = f'File detected: {filename}'
        if file_type == 'image':
            try:
                ocr_text = scanner.basic_ocr(file_path)
                if ocr_text and ocr_text.strip():
                    content_info = ocr_text.strip()
                    print(f"  OCR extracted from {filename}: {content_info[:60]}...")
            except Exception as e:
                print(f"  Warning: Could not extract OCR from {filename}: {e}")
        
        # Determine if it's an ad
        is_ad = any(keyword in filename.lower() for keyword in ['ad', 'advertisement', 'sponsored'])
        
        content_data.append((
            file_type, filename,
            1 if is_ad else 0, 0 if is_ad else 1,
            0, 0, 0, 'Unknown', content_info
        ))
    
    return content_data

""" 
The final `main()` function showcases the operations performed on the database. It creates a table, 
inserts placeholder data, scans for media files, and prints the resulting table. Additionally, it 
includes an if-else statement to handle the scenario where no media files are found.
"""
def main():
    """Main function to demonstrate database operations."""
    with get_db_connection('fbContentType.db') as conn:
        cursor = conn.cursor()
        print("Database connection opened and cursor created.")

        create_facebook_ads_table(cursor)
        print("Table 'fbContentType' created successfully.")

        clear_table(cursor)
        print("Cleared existing records from table.")

        # Insert placeholder data
        print(f"\nInserting placeholder sample data...")
        insert_multiple_fb_content_types(cursor, PLACEHOLDER_DATA)
        print(f"Successfully inserted {len(PLACEHOLDER_DATA)} placeholder records.")

        # Scan and insert files
        print(f"\nScanning '{SCAN_DIRECTORY}' for media files...")
        scanned_data = scan_files_for_ads(SCAN_DIRECTORY)
        
        if scanned_data:
            insert_multiple_fb_content_types(cursor, scanned_data)
            print(f"Successfully inserted {len(scanned_data)} scanned file records.")
        else:
            print(f"No media files found in '{SCAN_DIRECTORY}'.")
        
        print_table(cursor)
    
    print("\nDatabase connection closed and changes committed automatically.")
    print("Data saved to 'fbContentType.db' file.")


""" 
The `if __name__ == '__main__':` block ensures the `main()` function runs only when the script is executed directly, 
not when imported as a module. This practice is common in Python programming, allowing users to see how the script works.
"""
if __name__ == '__main__':
    main()
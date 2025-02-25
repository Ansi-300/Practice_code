import os
import collections
from pprint import pprint

# Define the Downloads folder path (Windows Fix)
download_path = r'G:\Demo'  # Use raw string

# Dictionary to store file types and filenames
filemapping = collections.defaultdict(list)

# Iterate through the files in the directory
for filename in os.listdir(download_path):
    file_path = os.path.join(download_path, filename)  # Full path

    if os.path.isfile(file_path):  # Ensure it's a file
        file_type = os.path.splitext(filename)[-1].lower().strip('.')  # Extract extension safely
        filemapping[file_type].append(filename)

# Print categorized files
pprint(dict(filemapping))  # Convert defaultdict to a normal dictionary for display

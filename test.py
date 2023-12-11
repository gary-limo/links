import os
import re

# Define the path to the text file containing the fields to search for
fields_file_path = 'fields.txt'

# Read the fields from the text file
with open(fields_file_path, 'r') as fields_file:
    fields_to_search = [line.strip() for line in fields_file]

# Define a function to search for fields in a SQL file
def search_fields_in_sql_file(file_path, fields_to_search):
    try:
        with open(file_path, 'r') as sql_file:
            sql_content = sql_file.read()
            for field in fields_to_search:
                if re.search(r'\b{}\b'.format(field), sql_content, re.IGNORECASE):
                    return file_path
    except Exception as e:
        pass
    return None

# Define a function to search for SQL files in all folders and subfolders
def search_sql_files(root_folder, fields_to_search):
    matching_files = []
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.sql'):
                file_path = os.path.join(foldername, filename)
                result = search_fields_in_sql_file(file_path, fields_to_search)
                if result:
                    matching_files.append(result)
    return matching_files

# Replace 'root_folder' with the folder where you want to start the search
root_folder = '/path/to/your/root/folder'
matching_files = search_sql_files(root_folder, fields_to_search)

if matching_files:
    print("Matching SQL files found:")
    for file_path in matching_files:
        print(file_path)
else:
    print("No matching SQL files found.")

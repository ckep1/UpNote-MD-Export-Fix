import os
import re
import shutil

# Get the current directory
directory = os.getcwd()

# Define a function to parse the categories from a file
def get_categories(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        if len(lines) >= 3 and lines[1].startswith('categories:'):
            category_line = lines[2].strip()
            category_line = category_line[1:].strip()
            categories = re.split(r'\s*\/\s*', category_line)
            return categories
    return None

# Define a function to organize the files into folders based on categories
def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and file_path.endswith('.md'):
            categories = get_categories(file_path)
            if categories:
                current_dir = directory
                for category in categories:
                    current_dir = os.path.join(current_dir, category)
                    if not os.path.exists(current_dir):
                        os.mkdir(current_dir)
                shutil.move(file_path, current_dir)
            
            #delete this part to leave out the Uncategorized folder
            else:
                uncategorized_dir = os.path.join(directory, 'Uncategorized')
                if not os.path.exists(uncategorized_dir):
                    os.mkdir(uncategorized_dir)
                shutil.move(file_path, os.path.join(uncategorized_dir, filename))

# Run the function to organize the files
organize_files(directory)
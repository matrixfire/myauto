import shelve
import pyperclip
import sys
import csv
import os

# Determine the directory of the script
script_dir = os.path.dirname(__file__)
# Set the directory for the database and CSV files
data_dir = os.path.join(script_dir, 'mcb')
# Create the directory if it does not exist
os.makedirs(data_dir, exist_ok=True)

# Adjust the filename for shelve to include the directory path
shelve_filename = os.path.join(data_dir, 'mcb')

# Open a shelve file to store the data
my_shelf = shelve.open(shelve_filename)

# Function to export data to a CSV file
def export_to_csv(filename):
    filepath = os.path.join(data_dir, filename)
    with open(filepath, 'w', newline='') as csvfile:
        fieldnames = ['key', 'value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key in my_shelf.keys():
            writer.writerow({'key': key, 'value': my_shelf[key]})

# Function to import data from a CSV file
def import_from_csv(filename):
    filepath = os.path.join(data_dir, filename)
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            my_shelf[row['key']] = row['value']

# Get the length of the command line arguments
arg_len = len(sys.argv)

if arg_len >= 2:
    action = sys.argv[1].lower()
    if action == 'save' and arg_len == 3:
        keyword = sys.argv[2]
        my_shelf[keyword] = pyperclip.paste()
    elif action == 'delete':
        keyword = sys.argv[2] if arg_len == 3 else None
        if keyword and keyword in my_shelf:
            del my_shelf[keyword]  # Delete specific keyword.
        elif not keyword:
            print("Keyword for deletion not specified.")
    elif action == 'list':
        formatted_list = "\n".join(f"{key}: {my_shelf[key]}" for key in my_shelf.keys())
        pyperclip.copy(formatted_list)
    elif action == 'export':
        filename = sys.argv[2] if arg_len == 3 else 'mydata.csv'
        export_to_csv(filename)
    elif action == 'import':
        filename = sys.argv[2] if arg_len == 3 else 'mydata.csv'
        import_from_csv(filename)
    elif action == 'flush':
        # Clear the shelve, deleting all keywords
        my_shelf.clear()
        print("All data cleared from the shelve.")
    else:
        if action in my_shelf:
            content = my_shelf[action]
            # Check if content has curly braces and replace the content within them
            if '{' in content and '}' in content:
                content_to_paste = pyperclip.paste()
                content = content.replace(content[content.find('{'):content.find('}')+1], content_to_paste)
            pyperclip.copy(content.strip().strip("\""))

# Always close the shelve file
my_shelf.close()

'''
About 
READING AND WRITING FILES
ORGANIZING FILES


'''


import os
import zipfile
import shutil


def process_zip_files(folder_path, include_string):
    # unfolder all zip files, and extract the folder including some string seperately!
    # Get the list of zip files in the specified folder
    zip_files = [f for f in os.listdir(folder_path) if f.endswith('.zip')]
    print(zip_files)
    # Process each zip file
    for zip_file in zip_files:
        # Create a folder name based on the zip file name
        unzip_folder = os.path.join(folder_path, os.path.splitext(zip_file)[0])

        # Unzip the contents
        with zipfile.ZipFile(os.path.join(folder_path, zip_file), 'r') as zip_ref:
            try:
                zip_ref.extractall(unzip_folder)
            except Exception as e:
                print(f'\n{zip_file} unzipping...error: \n{e}\n')
        # Correct file names if applicable
        for root, dirs, files in os.walk(folder_path, topdown=False):
            correct_names(root)
            


        # Find subfolders containing the include string
        matching_subfolders = [subfolder for subfolder in os.listdir(unzip_folder) if include_string in subfolder]


        # Create a new folder to move matching subfolders' content
        new_folder = os.path.join(folder_path, f"{os.path.splitext(zip_file)[0]}({include_string})")
        os.makedirs(new_folder, exist_ok=True)

        # Move content of matching subfolders to the new folder
        for matching_subfolder in matching_subfolders:
            source_path = os.path.join(unzip_folder, matching_subfolder)
            destination_path = new_folder
            for root, dirs, files in os.walk(source_path):
                for name in files + dirs:
                    shutil.move(os.path.join(root, name), os.path.join(destination_path, name))

        # Remove the original zip file
        os.remove(os.path.join(folder_path, zip_file))

        # Remove the unzipped folder
        shutil.rmtree(unzip_folder)
        print(f'{zip_file} finished.')




def rename_empty_folders(path):
    """
    Renames empty folders in the given path by appending '(empty)' to their names.
    
    Parameters:
        path (str): The path to check for empty folders.
    """
    for foldername, subfolders, filenames in os.walk(path):
        if not subfolders and not filenames:  # If the folder is empty
            new_name = os.path.join(os.path.dirname(foldername), "(empty) " + os.path.basename(foldername))
            shutil.move(foldername, new_name)
            print(f"Renamed '{foldername}' to '{new_name}'")


import os
import zipfile

def extract_all_zips(path):
    for filename in os.listdir(path)[:1]:
        if filename.endswith('.zip'):
            zip_file_path = os.path.join(path, filename)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(path)
            print(f"Extracted: {zip_file_path}")


import os
import zipfile
import shutil

def extract_all_zips(path):
    for filename in os.listdir(path):
        if filename.endswith('.zip'):
            zip_file_path = os.path.join(path, filename)
            folder_name = os.path.splitext(filename)[0]  # Extract folder name from zip file name
            folder_path = os.path.join(path, folder_name)
            os.makedirs(folder_path, exist_ok=True)  # Create folder to extract zip contents
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)  # Extract contents into the new folder
            print(f"Extracted: {zip_file_path} to {folder_path}")
            # Correct file names if applicable
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    os.rename(os.path.join(root, file), os.path.join(root, file.encode('cp437').decode('gbk')))  

# Example usage:
# extract_all_zips('/path/to/your/directory')





import os
import zipfile

def extract_all_zips(path):
    """
    Extracts all zip files found at the specified path.
    Creates a new folder named after each zip file (without the .zip extension)
    and extracts the contents of the zip file into this folder.
    Corrects both file and folder names with non-ASCII characters.

    Parameters:
        path (str): The path where zip files are located.
    """
    for filename in os.listdir(path):
        if filename.endswith('.zip'):
            zip_file_path = os.path.join(path, filename)
            folder_name = os.path.splitext(filename)[0]  # Extract folder name from zip file name
            folder_path = os.path.join(path, folder_name)
            os.makedirs(folder_path, exist_ok=True)  # Create folder to extract zip contents
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)  # Extract contents into the new folder
            print(f"Extracted: {zip_file_path} to {folder_path}")
            folders.append(folder_path)
            # Correct file and folder names recursively
            for root, dirs, files in os.walk(folder_path, topdown=False):
                try:
                    correct_names(root)
                except Exception as e:
                    print('Correcting names failed: \n {e}\n')
                else:
                    print(f'correct names at {root}')




def correct_names_(directory):
    """
    Recursively corrects both file and folder names within the specified directory.

    Parameters:
        directory (str): The path to the directory to correct names in.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            os.rename(
                os.path.join(root, file),
                os.path.join(root, file.encode('cp437').decode('gbk'))
            )
        for folder in dirs:
            os.rename(
                os.path.join(root, folder),
                os.path.join(root, folder.encode('cp437').decode('gbk'))
            )



def correct_names(directory):
    """
    Recursively corrects both file and folder names within the specified directory.

    Parameters:
        directory (str): The path to the directory to correct names in.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(root, file, sep='\nxxxxx\n')
            os.rename(*fix_characts(root, file))
        for folder in dirs:
            print(root,folder, sep='\nxxxxx\n')
            os.rename(*fix_characts(root, folder))


def fix_characts(root, file_name):
    old_name  = os.path.join(root, file_name)
    try:
        new_name = os.path.join(root, file_name.encode('cp437').decode('gbk'))
    except Exception as e:
        print(e)
        new_name = old_name
    return old_name, new_name



import os
import pyperclip

def pds(path, indent='', structure=''):
    """
    Prints the directory structure starting from the given path.
    """
    if os.path.isdir(path):
        structure += indent + os.path.basename(path) + '/\n'
        for item in sorted(os.listdir(path)):
            structure = pds(os.path.join(path, item), indent + '  ', structure)
    else:
        structure += indent + os.path.basename(path) + '\n'
    return structure

# - To read contents of a ZIP file in Python, create a `ZipFile` object using `zipfile.ZipFile()` function.
# - This object acts similarly to a `File` object returned by `open()`.
# - Use `ZipFile` object's `namelist()` method to get a list of all files and folders in the ZIP.
# - Obtain individual file information using `getinfo()` method, returning a `ZipInfo` object.
# - `ZipInfo` object provides attributes like `file_size` and `compress_size`, representing original and compressed sizes.
# - Calculate compression ratio with `original file size / compressed file size`.
# os.path.abspath('.'), os.listdir('.'), os.path.join(, ),  os.path.basename()



def backupToZip(folder):
    # Backup the entire contents of "folder" into a zip file.

    folder = os.path.abspath(folder) # Make sure folder is absolute

    # Figure out the filename this code should used based on what
    # files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the zip file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the zip file.
        backupZip.write(foldername)

        # Add all the files in this folder to the zip file.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # Don't backup the backup zip files.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


def backupToZip(folder):
    # Backup the entire contents of "folder" into a zip file.

    folder = os.path.abspath(folder) # Make sure folder is absolute

    # Figure out the filename this code should used based on what
    # files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the zip file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the zip file.
        backupZip.write(foldername)

        # Add all the files in this folder to the zip file.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # Don't backup the backup zip files.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')





def organize_folders(folder_path, final_folder="organized_files"):
    organize_folders_path = os.path.join(folder_path, final_folder)
    os.makedirs(organize_folders_path)
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        if not os.path.isdir(subfolder_path):
            continue
        for subfolder in os.listdir(subfolder_path):
            subfolder_path = os.path.join(subfolder_path, subfolder)
            shutil.move(subfolder_path, organize_folders_path)
            print(f'Moved {subfolder_path} -> {organize_folders_path}')
            

import os
import shutil

def organize_folders(folder_path, final_folder="organized_files"):
    organize_folders_path = os.path.join(folder_path, final_folder)
    os.makedirs(organize_folders_path, exist_ok=True)  # Create final folder if it doesn't exist

    # Move files directly within folder_path to final_folder
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            shutil.move(item_path, organize_folders_path)
            print(f'Moved {item_path} -> {organize_folders_path}')

    # Move files within subfolders to final_folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            shutil.move(file_path, organize_folders_path)
            print(f'Moved {file_path} -> {organize_folders_path}')

# Example usage:
organize_folders('/path/to/your/folder')



if __name__ == "__main__":
    # Specify the folder path and include string
    # folder_path = input("Enter the folder path: ")
    # include_string = input("Enter the include string: ")
    folder_path = r'C:\Users\34950\Desktop\full_time_work\temp\ttttt'
    include_string = '高清' # 高清
    # Call the function
    process_zip_files(folder_path, include_string)
    # backupToZip(r'C:\Users\34950\Desktop\full_time_work\myauto\33028详情页')





# Summary:
# - `os.unlink(path)`: Deletes a file.
# - `os.rmdir(path)`: Deletes an empty folder.
# - `shutil.rmtree(path)`: Deletes a folder and all its contents.
# - `send2trash`: Sends files and folders to the computer's trash/recycle bin, offering a safer deletion option.
# Absolute vs. Relative Paths:  The .\ at the start of a relative path is optional. For example, .\spam.txt and spam.txt refer to the same file; dot this directory, dot-dot the parent folder.
# os.makedirs()； Path(r'C:\Users\Al\spam').mkdir() Note that mkdir() can only make one directory at a time; it won’t make several subdirectories at once like os.makedirs().
# os.path.abspath(); os.path.isabs(); os.path.relpath(, )
# os.path.split() is the same as (os.path.dirname(), os.path.basename())
# os.path.getsize(); os.listdir()
# list(some_path_obj.glob('*.?x?'); both os.listdir(p) or p.glob('*') does the same.
# p.exists(); p.is_file(); p.is_dir()
    

def walk(path):
    import os
    for folderName, subfolders, filenames in os.walk(path):
        print('The current folder is ' + folderName)
        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': '+ filename)
        print("\n"*3)



import os
import shutil
import random
def move_contents_to_result_folder(path, result_folder):
    # Walk through the directory tree rooted at 'path'
    for root, dirs, files in os.walk(path):
        # Get the relative path from the source folder, skipping the first level
        relative_path = os.path.relpath(root, path)
        relative_path = relative_path.split(os.path.sep, 1)[-1]

        # Construct the destination folder path
        dest_folder = os.path.join(result_folder, relative_path)

        # Create the destination folder if it doesn't exist
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # Move files to the destination folder while preserving the directory structure
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_folder, file)
            try:
                shutil.move(src_file, dest_file)
            except Exception as e:
                dest_file = os.path.join(dest_folder, f'({str(random.random())})' + file)
                print(e, "renamed")
            print(f"Move {src_file} -> {dest_file}")

# Example usage:




source_folder = r'C:\Users\34950\Desktop\test3'
result_folder = r'C:\Users\34950\Desktop\test4'
move_contents_to_result_folder(source_folder, result_folder)




def copy_jpg_images(source_folder, result_folder):
    # Create the result folder if it doesn't exist
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # Walk through the directory tree rooted at 'source_folder'
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.jpg'):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(result_folder, file)

                # If a file with the same name exists in the result folder, rename it
                if os.path.exists(dest_file):
                    base_name, extension = os.path.splitext(file)
                    new_file_name = f"{base_name} (copied){extension}"
                    dest_file = os.path.join(result_folder, new_file_name)

                # Copy the file to the result folder
                shutil.copy(src_file, dest_file)



'''

import shelve

# Saving variables to a binary shelf file
def save_data():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    with shelve.open('data.shelf') as shelf_file:
        shelf_file['data'] = data

# Restoring data from the binary shelf file
def load_data():
    with shelve.open('data.shelf') as shelf_file:
        data = shelf_file.get('data', {})
        print("Loaded data:", data)

        
def save_data():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    with open('data.py', 'w') as file:
        file.write("variable = " + pprint.pformat(data))

def load_data():
    import data
    print("Loaded data:", data.variable)
        
# Save data to shelf file
save_data()

# Load data from shelf file
load_data()



'''


import random as r
def c(choices_list=["work", "learn"], weight_list=[30, 10]):
    what_2_do = r.choice(choices_list)
    index = choices_list.index(what_2_do)
    time_2_do = r.randint(weight_list[index]//2, weight_list[index])
    print(f'I decide to {what_2_do.title()} for {time_2_do} mins.')

# c()
    

def copy_first_images(input_path, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get all subfolders within the input path
    subfolders = [folder for folder in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, folder))]

    for folder in subfolders:
        # Join subfolder with relative path "主图\2000X2667"
        subfolder_path = os.path.join(input_path, folder, "主图", "2000X2667")

        # Print the joined path for verification
        print("Joined path:", subfolder_path)

        # Check if the joined path exists
        if os.path.exists(subfolder_path):
            # Get all files in the joined path
            files = os.listdir(subfolder_path)
            
            # Filter out only image files (assuming images have extensions like .jpg, .png, etc.)
            image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

            # If there are image files in the folder, copy the first image to the output folder
            if image_files:
                # Get the path of the first image file
                first_image_path = os.path.join(subfolder_path, image_files[0])

                # Copy the first image file to the output folder
                shutil.copy(first_image_path, output_folder)
                print("Copied", image_files[0], "to", output_folder)
            else:
                print("No image files found in", subfolder_path)
        else:
            print("Path does not exist:", subfolder_path)
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
            zip_ref.extractall(unzip_folder)

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




if __name__ == "__main__":
    # Specify the folder path and include string
    # folder_path = input("Enter the folder path: ")
    # include_string = input("Enter the include string: ")
    folder_path = r'C:\Users\34950\Desktop\full_time_work\temp\imgs12'
    include_string = '高清' # 高清
    # Call the function
    # process_zip_files(folder_path, include_string)
    # backupToZip(r'C:\Users\34950\Desktop\full_time_work\myauto\33028详情页')





# Summary:
# - `os.unlink(path)`: Deletes a file.
# - `os.rmdir(path)`: Deletes an empty folder.
# - `shutil.rmtree(path)`: Deletes a folder and all its contents.
# - `send2trash`: Sends files and folders to the computer's trash/recycle bin, offering a safer deletion option.
import os
import zipfile
import shutil


def process_zip_files(folder_path, include_string):
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


if __name__ == "__main__":
    # Specify the folder path and include string
    # folder_path = input("Enter the folder path: ")
    # include_string = input("Enter the include string: ")
    folder_path = r'C:\Users\34950\Desktop\full_time_work\temp\imgs2'
    include_string = '高清'
    # Call the function
    process_zip_files(folder_path, include_string)



# if __name__ == "__main__":
#     # Specify the folder path and exclude string
#     # folder_path = input("Enter the folder path: ")
#     # exclude_string = input("Enter the exclude string: ")
#     folder_path = r'C:\Users\34950\Desktop\full_time_work\temp\test'
#     exclude_string = '高清'
#     # Call the function
#     unzip_and_delete(folder_path, exclude_string)

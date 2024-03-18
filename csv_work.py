import csv
from pathlib import Path
import os
import re
import json


# 1, getting data from my own cache csv products data, and generate the data list 
def read_from_csv_customize(input_file, fieldnames=['货号', '品名', '尺寸', '单价', '零件数量', 'Type']):
    '''
    read from my customized csv file, namely my own cache file!
    '''
    result_data = []
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            filtered_row = {key: row[key] for key in fieldnames if key in row}
            model_id = filtered_row['货号']
            pcs_num = filtered_row['零件数量']
            dimension = filtered_row['尺寸']
            tmp = f'''
<p data-mce-fragment="1"><span data-mce-fragment="1">Item : Reobrix {model_id}</span></p>
<p data-mce-fragment="1"><span data-mce-fragment="1">Number of Pieces : {pcs_num} <br></span></p>
<p data-mce-fragment="1"><span data-mce-fragment="1">Dimensions(L x W x H) : {dimension} CM</span></p>
<p data-mce-fragment="1"><span data-mce-fragment="1">Package Type: Carton (w</span>ithout original box)</p>
<p data-mce-fragment="1"><strong data-mce-fragment="1">Note: <span style="color: #ff2a00;">The Mini Figures are <span style="text-decoration: underline;">NOT INCLUDED</span> in this Set !</span></strong></p>
'''
            new_data_dict = {}
            new_data_dict['Handle'] = 'reobrix-' + str(filtered_row['货号']) + '-' + filtered_row['品名']
            new_data_dict['Title'] = 'Reobrix ' +  filtered_row['品名'].title()
            new_data_dict['Variant SKU'] = str(filtered_row['货号'])
            new_data_dict['Variant Price'] = str(filtered_row['单价'])
            new_data_dict['Body (HTML)'] = tmp
            new_data_dict['Tags'] = filtered_row['Type']
            result_data.append(new_data_dict)
    return result_data


# 2, based on data and template to generate the preparing uploading file
def modify_csv(input_file, data_list, output_file=''):
    # Read the existing CSV file
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        header = reader.fieldnames # getting headers in a list

        # Prepare data for writing
        rows_to_write = []
        for data_dict in data_list: # data_list is a list of dictionaries
            # Ensure the keys in data_dict match the header
            row = {key: data_dict.get(key, '') for key in header}
            rows_to_write.append(row)
        print(rows_to_write)
    if not output_file:
        dir, old_fn = os.path.split()
        output_file = os.path.join(dir,"data_populated_"+old_fn)
    # Write to a new CSV file
    with open(output_file, 'a', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=header)
        
        # Write the header
        writer.writeheader()

        # Write the rows from the provided data_list
        writer.writerows(rows_to_write)
        print(f'Filed saved at {output_file}.')




existing_csv_file_ = r'C:\Users\34950\Desktop\full_time_work\products_list.csv' # this is my customized template

data_to_append = read_from_csv_customize(existing_csv_file_)


existing_csv_file = r'C:\Users\34950\Desktop\full_time_work\product_template.csv' # this is offical template, but only to get the format


new_csv_file = 'new_data.csv'

modify_csv(existing_csv_file, data_to_append, new_csv_file)






path = Path(r'C:\Users\34950\Desktop\full_time_work\myauto') / 'data.json'
my_dict = json.loads(path.read_text())

def sanitize_file_name(file_name):
    invalid_chars = '\\/:*?"<>|'
    found = False
    new_file_name = file_name
    for char in invalid_chars:
        if char in file_name:
            new_file_name = new_file_name.replace(char, ' ')
            found = True
    if found:
        print(f"Sanitize name {file_name}->{new_file_name}")
    return new_file_name


def rename_images_in_folders(path, mapping_dict):
    import random
    for folder_name in os.listdir(path):
        folder_path = os.path.join(path, folder_name)
        if os.path.isdir(folder_path):
            # Use regex to extract leading digits from the folder name
            match = re.match(r'^(\d+)', folder_name)
            if match:
                leading_digits = match.group(1)
                key = leading_digits
                # Check if the key exists in the dictionary
                if key in mapping_dict:
                    value = mapping_dict[key]
                    # Iterate through files in the folder and its subfolders
                    for root, dirs, files in os.walk(folder_path):
                        for filename in files:
                            file_path = os.path.join(root, filename)
                            # Check if the file is an image (jpg or png)
                            if filename.lower().endswith(('.jpg', '.png')):
                                # Create the new filename by appending the value and "-"
                                new_filename =sanitize_file_name(f"{value.strip().title()}-{filename}") # -{filename} {random.randint(1000, 9999)}
                                new_file_path = os.path.join(root, new_filename)
                                # Rename the file
                                try:
                                    os.rename(file_path, new_file_path)
                                except Exception as e:
                                    print(f'\nError for {file_path}: {e}')


# rename_images_in_folders(r'C:\Users\34950\Desktop\full_time_work\temp\imgs12', my_dict)

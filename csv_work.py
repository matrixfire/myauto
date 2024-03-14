import csv

def modify_csv(input_file, data_list, output_file):
    # Read the existing CSV file
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        header = reader.fieldnames

        # Prepare data for writing
        rows_to_write = []
        for data_dict in data_list:
            # Ensure the keys in data_dict match the header
            row = {key: data_dict.get(key, '') for key in header}
            rows_to_write.append(row)
        print(rows_to_write)
    # Write to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=header)
        
        # Write the header
        writer.writeheader()

        # Write the rows from the provided data_list
        writer.writerows(rows_to_write)


def read_from_csv(input_file, fieldnames):
    result_data = []
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        
        for row in reader:
            filtered_row = {key: row[key] for key in fieldnames if key in row}
            result_data.append(filtered_row)
    return result_data





def read_from_csv_customize(input_file, fieldnames=['货号', '品名', '尺寸', '单价', '零件数量', 'Type']):
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

# Example usage:
existing_csv_file_ = r'C:\Users\34950\Desktop\full_time_work\products_list.csv'
# desired_fieldnames = ['货号', '品名', '尺寸', '单价']

data_read = read_from_csv_customize(existing_csv_file_)


existing_csv_file = r'C:\Users\34950\Desktop\full_time_work\product_template.csv'
data_to_append = data_read


new_csv_file = 'new_data.csv'

modify_csv(existing_csv_file, data_to_append, new_csv_file)



def read_from_csv(input_file=r'C:\Users\34950\Desktop\full_time_work\products_list.csv'):
    import re, csv
    re_obj = re.compile(r'.*?[(（](.*?)[)）]', re.DOTALL)
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        # header = reader.fieldnames
        print(reader.fieldnames)
        data_lt = []
        for row in reader:
            data = row["品名(ori)"]
            new_data_mo = re_obj.search(data)
            if new_data_mo:
                new_data = new_data_mo.group(1)
                print(new_data)
            else:
                new_data = "failed" 
            data_lt.append(new_data)
        print(data_lt[:10])
    import pyperclip as p
    p.copy('\n'.join(data_lt))


def t():
    import pyperclip as p
    import re
    lines = p.paste().strip().split("\r\n")
    cleaned_lines = list(map(lambda line: line.strip().title(), lines))
    re_obj = re.compile(r'^([^（]+)')
    new_list = []
    print(cleaned_lines[:10])
    for i in cleaned_lines:
        item_mo = re_obj.search(i)
        if item_mo == None:
            item = ""
        else:
            item = item_mo.group(1)
        new_list.append(item.strip())
    p.copy('\n'.join(new_list))


def gc(): # get_data_from_clipboard
    import pyperclip as p
    txt = p.paste().strip()
    # pattern = re.compile(r'\d+|"\d+\n\d+"')
    pattern = re.compile(r'\D*\d+\D*|"\D*\d+\D*\n\D*\d+\D*"')
    dlt = txt.split('\n')
    # dlt = pattern.findall(txt)
    print(f"Data found: {len(dlt)}")
    return dlt

data_dict = dict(zip(a, b))







from pathlib import Path
import os
import re
import json


path = Path(r'C:\Users\34950\Desktop\full_time_work\myauto') / 'data.json'
my_dict = json.loads(path.read_text())

def rename_images_in_folders(path, mapping_dict):
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
                                new_filename = f"{value.strip().title()}-{filename}"
                                new_file_path = os.path.join(root, new_filename)
                                # Rename the file
                                try:
                                    os.rename(file_path, new_file_path)
                                except:
                                    print(f'Error for {file_path}')


rename_images_in_folders(r'C:\Users\34950\Desktop\full_time_work\temp\imgs7', my_dict)

import pyperclip as p
import re


def ec():
    import pyperclip as p
    import re
    txt = p.paste()
    # Use the Unicode character range for Chinese characters
    re_obj = re.compile(r'\s*([\u4e00-\u9fff]+系列)', re.MULTILINE) 
    data_lt = re_obj.findall(txt)

    total_words= ''
    print(data_lt, type(data_lt))
    for words in data_lt:
        total_words += (words+'\n')

    p.copy(total_words)
    print(total_words)


from PyPDF2 import PdfReader, PdfWriter

def resize_pdf(input_pdf_path, output_pdf_path, scale_factor=0.5):
    """
    Resize a PDF by a given scale factor (default is 0.5).
    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_path: Path to save the resized PDF.
    :param scale_factor: Scale factor (0.0 to 1.0) to resize the PDF.
    """
    with open(input_pdf_path, 'rb') as input_pdf:
        pdf_reader = PdfReader(input_pdf)
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page.scale_by(scale_factor)  # Corrected method name
            pdf_writer.add_page(page)

        with open(output_pdf_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

# Example usage: Resize "Reobrix_EN.pdf" to a smaller size and save as "output.pdf"
# resize_pdf("Reobrix_EN.pdf", "output.pdf", scale_factor=0.7)
print("PDF resized successfully. Saved as output.pdf")

import PyPDF2

def read_pdf(file_path):
    pdf_reader = PyPDF2.PdfReader(file_path)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

file_path = 'Reobrix_EN.pdf'
text = read_pdf(file_path)
print(text)


# file_path = 'Reobrix_EN.pdf'
# text = read_pdf(file_path)
# print(text)



import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
# The reader object can be looped over only once. To reread the CSV file, you must call csv.reader to create a reader object.
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row)) # To get the row number, use the reader object’s line_num variable


# Open the output file for writing
outputFile = open('output.csv', 'w', newline='') # On Windows, you’ll also need to pass a blank string for the open() function’s newline keyword argument

# Create a CSV writer object
outputWriter = csv.writer(outputFile) #  delimiter='\t', lineterminator='\n\n' separate cells with a tab character instead of a comma and you want the rows to be double-spaced

# Write rows to the CSV file
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])

# Close the output file
outputFile.close()




# Open the CSV file with a header
exampleFile = open('exampleWithHeader.csv')

# Create a CSV DictReader object
exampleDictReader = csv.DictReader(exampleFile)

# Iterate through rows and print specific columns
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])

# Close the file
exampleFile.close()





# Open the CSV file
exampleFile = open('example.csv')

# Create a CSV DictReader object with specified field names
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount']) # fieldnames=['time', 'name', 'amount']

# Iterate through rows and print specific columns
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])

# Close the file
exampleFile.close()






# Open the output file for writing
outputFile = open('output.csv', 'w', newline='')

# Create a CSV DictWriter object with specified field names
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])

# Write the header to the CSV file
outputDictWriter.writeheader()

# Write rows to the CSV file
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})

# Close the output file
outputFile.close()


# .replace("*", " x "); model_id, pcs_num, dimension


tmp = 

'''
<p data-mce-fragment="1"><span data-mce-fragment="1">Item : Reobrix {model_id}</span></p>
<p data-mce-fragment="1"><span data-mce-fragment="1">Number of Pieces : {pcs_num} <br></span></p>
<p data-mce-fragment="1"><span data-mce-fragment="1">Dimensions(L x W x H) : {dimension} CM</span></p>
<p data-mce-fragment="1"><span data-mce-fragment="1">Package Type: Carton (w</span>ithout original box)</p>
<p data-mce-fragment="1"><span data-mce-fragment="1">Include instruction book, Miniatur Guns and Weapons included,<br data-mce-fragment="1"></span></p>
<p data-mce-fragment="1"><strong data-mce-fragment="1">Note: <span style="color: #ff2a00;">The Mini Figures are <span style="text-decoration: underline;">NOT INCLUDED</span> in this Set !</span></strong></p>
'''
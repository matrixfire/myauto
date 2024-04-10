'''
MANIPULATING IMAGES

Photos

need to edit a massive number of images


Pillow: crop, resize, and edit the content of an image
All the rotations, resizing, cropping, drawing, and other image manipulations will be done through method calls on this Image object.

The origin is the pixel at the top-left corner of the image and is specified with the notation (0, 0). 
Coordinates and Box Tuples: Many of Pillow’s functions and methods take a box tuple argument, like (3, 1, 9, 6), which is (Left, Top, Right, Bottom).
'''
from PIL import Image, ImageColor, ImageDraw
import os


aIm = Image.open('zophie.png')
aIm.save('zophie.jpg')

width, height = aIm.size
# catIm.format_description
print(f"{aIm.filename}, {aIm.format}")



def gis(image_path):
    with Image.open(image_path) as img:
        return img.size

cIm = aIm.crop((335, 345, 565, 560)) # exclusive
cIm.save('cropped.png')

dIm = aIm.copy()
dIm.paste(cIm, (0, 0))

x, y = dIm.size[0]-cIm.size[0], dIm.size[1]-cIm.size[1]
dIm.paste(cIm, (x, y))


eIm = aIm.resize((int(width / 2), int(height / 2)))
eIm.save('quartersized.png')


aIm.rotate(90).save('rotated90.png')

fIm = aIm.rotate(7, expand=True)
fIm.save('rotated7_expanded.png')

gIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
gIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')







def merge_and_save_images_corrected(base_image_path, second_image_path, factor=0.7):
    """
    Adjusts the function to resize the second image to 61.8% of the base image's height, ensuring the resized second
    image is pasted within the right side of the base image. The center of the second image will be equidistant from
    the upper, lower, and right side of the base image. This version also ensures the spacing on the right side of the
    base image is the same as the spacing to the sides of the second image. The final image is saved over the base image
    path, effectively updating the original base image.
    """
    from PIL import Image

    # Open the base image
    with Image.open(base_image_path) as base_img:
        base_width, base_height = base_img.size
        print(f"Base image size: {base_img.size}")

        # Open the second image and resize it to 61.8% of the base image's height
        with Image.open(second_image_path) as second_img:
            resize_height = int(base_height * factor)
            second_img_resized = second_img.resize((resize_height*second_img.size[0]//second_img.size[1], resize_height))

            # Calculate the position to paste the resized second image
            # Ensure it's within the base image and equidistant from the top, bottom, and right edge
            spacing = (base_height - resize_height) // 2
            x_position = base_width - resize_height - spacing
            y_position = spacing

            # Paste the resized second image onto the base image at the calculated position
            base_img.paste(second_img_resized, (x_position, y_position))

            # Save the modified image back to the base image path
            new_base_image_path = 'new_' + base_image_path
            base_img.save(new_base_image_path)


def merge_and_save_images_corrected_lt(base_image_path, second_image_path_lt, factor=0.7):
    """
    Adjusts the function to resize the second image to 61.8% of the base image's height, ensuring the resized second
    image is pasted within the right side of the base image. The center of the second image will be equidistant from
    the upper, lower, and right side of the base image. This version also ensures the spacing on the right side of the
    base image is the same as the spacing to the sides of the second image. The final image is saved over the base image
    path, effectively updating the original base image.
    """
    from PIL import Image

    # Open the base image
    with Image.open(base_image_path) as base_img:
        base_width, base_height = base_img.size
        print(f"Base image size: {base_img.size}")
        base_width_ = base_width
        # Open the second image and resize it to 61.8% of the base image's height
        for second_image_path in second_image_path_lt:
            print(second_image_path)
            with Image.open(second_image_path) as second_img:
                resize_height = int(base_height * factor)
                second_img_resized = second_img.resize((resize_height*second_img.size[0]//second_img.size[1], resize_height))

                # Calculate the position to paste the resized second image
                # Ensure it's within the base image and equidistant from the top, bottom, and right edge
                spacing = (base_height - resize_height) // 2
                x_position = base_width_ - resize_height - spacing
                y_position = spacing

                # Paste the resized second image onto the base image at the calculated position
                base_img.paste(second_img_resized, (x_position, y_position))

                # Save the modified image back to the base image path
                new_base_image_path = 'new_' + base_image_path
            base_width_ -= resize_height*second_img.size[0]//second_img.size[1] *1.2
            base_width_ = int(base_width_)
        base_img.save(new_base_image_path)




def _merge_and_save_images_corrected(base_image_path, second_image_path, factor=0.7):
    """
    Adjusts the function to resize the second image to 61.8% of the base image's height, ensuring the resized second
    image is pasted within the right side of the base image. The center of the second image will be equidistant from
    the upper, lower, and right side of the base image. This version also ensures the spacing on the right side of the
    base image is the same as the spacing to the sides of the second image. The final image is saved over the base image
    path, effectively updating the original base image.
    """
    from PIL import Image

    # Open the base image
    with Image.open(base_image_path) as base_img:
        base_width, base_height = base_img.size
        print(f"Base image size: {base_img.size}")

        # Open the second image and resize it to 61.8% of the base image's height
        with Image.open(second_image_path) as second_img:
            resize_height = int(base_height * factor)
            second_img_resized = second_img.resize((resize_height, resize_height))

            # Calculate the position to paste the resized second image
            # Ensure it's within the base image and equidistant from the top, bottom, and right edge
            spacing = (base_height - resize_height) // 2
            x_position = base_width - resize_height - spacing-resize_height
            y_position = spacing

            # Paste the resized second image onto the base image at the calculated position
            base_img.paste(second_img_resized, (x_position, y_position))

            # Save the modified image back to the base image path
            new_base_image_path = 'new_' + base_image_path
            base_img.save(new_base_image_path)

# Note: To use this function, replace 'base_image_path' and 'second_image_path' with your actual image paths.
# This code will not run here due to the absence of actual file paths and images.
# Example usage:
# base_image_path = "/path/to/your/base/image.jpg"
# second_image_path = "/path/to/your/second/image.jpg"
# merge_and_save_images_corrected(base_image_path, second_image_path)
# The modified base image will be saved over the original file.

# Example usage
# base_image_path = "/path/to/base/image.jpg"
# second_image_path = "/path/to/second/image.jpg"
# modified_image = merge_images_within_base(base_image_path, second_image_path)
# modified_image.show() # This will display the base image with the second image merged within its right side.


# Example usage
# base_image_path = "/path/to/base/image.jpg"
# second_image_path = "/path/to/second/image.jpg"
# new_image = merge_images(base_image_path, second_image_path)
# new_image.show() # This will display the new image with the modifications.




















def change_individual_pixels():
    # Create a new RGBA image with dimensions 100x100
    im = Image.new('RGBA', (100, 100))
    # bIm = Image.new('RGBA', (100, 200), 'purple') # ('purple' can be omitted which means Invisible black, (0, 0, 0, 0), is the default color used if no color argument is specified
    # Set the pixels in the top half of the image to (210, 210, 210, 255)
    for x in range(100):
        for y in range(50):
            im.putpixel((x, y), (210, 210, 210, 255))
    # Set the pixels in the bottom half of the image to 'darkgray'
    for x in range(100):
        for y in range(50, 100):
            im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
            # get RGBA values from color name
            # ImageColor.getcolor('red', 'RGBA') # case-insensitive
    # Print the pixel values at specific coordinates
    print(im.getpixel((0, 0)))    # (210, 210, 210, 255)
    print(im.getpixel((0, 50)))   # (169, 169, 169, 255)
    # Save the image
    im.save('putPixel.png')




# tile Zophie’s head across the entire image
def tile_object_across_background(background_path, object_path, output_path):
    # Open the images
    background = Image.open(background_path)
    obj = Image.open(object_path)
    # Get image dimensions
    background_width, background_height = background.size
    obj_width, obj_height = obj.size
    # Create a copy of the background image
    result_image = background.copy()
    # Iterate over positions and paste the object image
    for left in range(0, background_width, obj_width):
        for top in range(0, background_height, obj_height):
            result_image.paste(obj, (left, top))
    # Save the result
    result_image.save(output_path)

# the boring job of resizing thousands of images and adding a small logo watermark to the corner of each.
    




def resize_and_add_logo(input_dir='.', output_dir='withLogo', square_fit_size=300, logo_filename='catlogo.png'):
    # Load the logo image
    logo_im = Image.open(logo_filename)
    logo_width, logo_height = logo_im.size
    print(f"Logo dimensions: {logo_width} x {logo_height}")
    # Create a directory to store images with logos
    os.makedirs(output_dir, exist_ok=True)
    # Loop over all files in the input directory
    for filename in os.listdir(input_dir):
        # Skip non-image files and the logo file itself
        if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_filename:
            continue
        # Open the image
        im = Image.open(os.path.join(input_dir, filename))
        width, height = im.size
        print(f"Original image dimensions: {width} x {height}")
        ori_width, ori_height = width, height
        # Check if the image needs to be resized
        if width > square_fit_size or height > square_fit_size:
            # Calculate the new width and height to resize to
            if width > height:
                height = int((square_fit_size / width) * height)
                width = square_fit_size
            else:
                width = int((square_fit_size / height) * width)
                height = square_fit_size
            # Resize the image
            print(f'Resizing {filename}... from original ({ori_width}, {ori_height}) to ({width}, {height}).')
            im = im.resize((width, height))
        # Add the logo to the lower-right corner
        print(f'Adding logo to {filename}...')
        logo_im_resized = logo_im.resize((int(min(width, height) * 1/10), int(min(width, height) * 1/10 * logo_height/logo_width)))
        logo_resized_width, logo_resized_height = logo_im_resized.size
        im.paste(logo_im_resized, (width - logo_resized_width, height - logo_resized_height), logo_im_resized)
        # Save changes
        im.save(os.path.join(output_dir, filename))

# Example usage
# resize_and_add_logo(input_dir='.', output_dir='withLogo', square_fit_size=300, logo_filename='catlogo.png')




def get_size(size, required_dimension):
    a, b = size
    if max(a, b) > required_dimension:
        return size
    else:
        if a >b:
            return (required_dimension, required_dimension*b//a)
        else:
            return (required_dimension*a//b, required_dimension)
    

def resize_images(input_folder, output_folder, size=(200, 200)):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    # Iterate over all files in the input folder
    for file_name in os.listdir(input_folder):
        # Get the full path of the file
        file_path = os.path.join(input_folder, file_name)
        # Check if the file is an image (you can extend this check if needed)
        if os.path.isfile(file_path) and file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            # Open the image using PIL
            try:
                with Image.open(file_path) as img:

                    size = get_size(img.size, 3000)
                    # Resize the image
                    img_resized = img.resize(size)
                    
                    # Get the file name (without extension) and extension
                    file_name_no_ext, file_ext = os.path.splitext(file_name)
                    
                    # Construct the output file path
                    output_file_path = os.path.join(output_folder, f"{file_name_no_ext}_resized{file_ext}")

                    # Save the resized image to the output folder
                    img_resized.save(output_file_path)
                    print(f"Resized image saved: {output_file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        else:
            print(f"Skipping {file_path}. Not an image file.")


a_d = r'C:\Users\34950\Desktop\test3\1'
b_d = r'C:\Users\34950\Desktop\test3'
resize_images(a_d, b_d)
'''PATTERN MATCHING WITH REGULAR EXPRESSIONS


ttps://pythex.org/.

'''





'''
My work:
Ideas for Similar Programs
Being able to composite images or modify image sizes in a batch can be useful in many applications. You could write similar programs to do the following:

Add text or a website URL to images.
Add timestamps to images.
Copy or move images into different folders based on their sizes.
Add a mostly transparent watermark to an image to prevent others from copying it.'''



# Create a new RGBA image with a white background
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

# Draw a black square
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')

# Draw a blue rectangle
draw.rectangle((20, 30, 60, 60), fill='blue')

# Draw a red ellipse (or circle in this case)
draw.ellipse((120, 30, 160, 60), fill='red')

# Draw a brown polygon
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')

# Draw green lines
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')

# Save the image
im.save('drawing.png')



from PIL import Image, ImageDraw, ImageFont
import os

# Create a new RGBA image with a white background
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

# Draw text using the default font
draw.text((20, 150), 'Hello', fill='purple')

# Specify a custom font (Arial in this case)
fonts_folder = 'FONT_FOLDER'  # Replace with the actual path to your font folder
arial_font_path = os.path.join(fonts_folder, 'arial.ttf')
arial_font = ImageFont.truetype(arial_font_path, 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arial_font)

# Save the image
im.save('text.png')







def make_66_plans():
    import pyperclip as p
    import random as r
    text = p.paste().strip()
    lines = text.split('\n')
    print(f'Lines found: {len(lines)}')
    if len(lines) < 36:
        lines.extend(["contiue"]*(36-len(lines)))
    r.shuffle(lines)
    pre_plans = lines[:36]
    plans = []
    for i in range(1,7):
        for j in range(1, 7):
            plans.append(f"D{i}{j}-{pre_plans.pop()}")
    print(plans)
    txt = '\n'.join(plans).strip()
    p.copy(txt)

    
import re
phoneNumRegex = re.compile(r'((\d\d\d)|(\(\d\d\d\))-)?(\d\d\d-\d\d\d\d)') # The first set of parentheses in a regex string will be group 1
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo = phoneNumRegex.search('My number is (415)-555-4242.')
mo = phoneNumRegex.search('My number is 555-4242.')
print(f'{mo.group(1)}, {mo.group(0)}, {mo.group()}, {mo.groups()}')
# Passing 0 or nothing to the group() method will return the entire matched text. 
# If you would like to retrieve all the groups at once, use the groups() method

def magic(temp):
    ts = temp.group(1)
    ts_all = temp.group()
    return rf"{ts}{'*'*(len(ts_all)-7)}"

sample_str =  'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****',sample_str)
agentNamesRegex.sub(magic, sample_str)
agentNamesRegex.sub(lambda mo:mo.group(1).title(), sample_str)

def m():
    import pyperclip as p
    import re
    original_txt = p.paste()
    re_obj = re.compile(r'第(\d)章')
    re_obj = re.compile(r'\d,\s+\w*.+')
    re_obj = re.compile(r"\{% static '(.*?)' %\}") # {% static 'css/nucleo-icons.css' %}
    new_txt = re_obj.sub(r"{% static 'new_/\1' %}", original_txt)
    # txt_lt = re_obj.findall(original_txt)
    p.copy(new_txt)
    # p.copy('\n'.join(txt_lt).strip())

def reverse_lines_in_clipboard():
    import pyperclip
    # Get text from clipboard
    clipboard_text = pyperclip.paste()

    # Split the text into lines and reverse their order
    lines = clipboard_text.splitlines()
    reversed_lines = reversed(lines)

    # Join the reversed lines and set the result back to the clipboard
    reversed_text = '\n'.join(reversed_lines)
    pyperclip.copy(reversed_text)

def magic_lines():
    import pyperclip
    # Get text from clipboard
    clipboard_text = pyperclip.paste()
    # Split the text into lines and reverse their order
    lines = clipboard_text.splitlines()
    new_lines = list(filter(lambda x: "import" in x, lines))
    # Join the reversed lines and set the result back to the clipboard
    new_text = '\n'.join(new_lines)
    pyperclip.copy(new_text)



import os

def extract_and_combine_py_files(folder_path, output_file):
    """
    Extracts all .py files from the specified folder and its subdirectories,
    excluding .pyc files and the 'myenv' directory, and combines them into a single output file.
    """
    with open(output_file, 'w') as outfile:
        for root, dirs, files in os.walk(folder_path):
            # Exclude 'myenv' directory and its subdirectories
            if 'myenv' in dirs:
                dirs.remove('myenv')
            for filename in files:
                if filename.endswith('.py') and not filename.endswith('.pyc'):
                    file_path = os.path.join(root, filename)
                    with open(file_path, 'r') as infile:
                        outfile.write(infile.read())
                        outfile.write('\n' + '_' * 30 + "\n\n")  # Add a newline separator between files
                    print(f'Finished {filename}!')

# Example usage:
folder_to_extract = '/path/to/your/folder'
output_filename = 'combined_python_files.py'
extract_and_combine_py_files(folder_to_extract, output_filename)
print(f"Combined .py files saved to {output_filename}")


'''


PATTERN MATCHING WITH REGULAR EXPRESSIONS
https://pythex.org/


1, In regular expressions, the following characters have special meanings: 
.  ^  $  *  +  ?  {  }  [  ]  \  |  (  )

2, Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible.
The non-greedy (also called lazy) version of the braces, which matches the shortest string possible, has the closing brace followed by a question mark.
"?" has 2 meaning: non-greedy match, optional group


3, To summarize what the findall() method returns, remember the following:

When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, the method findall() returns a list of string matches, such as ['415-555-9999', '212-555-0000'].
When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\d\d\d), the method findall() returns a list of tuples of strings (one string for each group), such as [('415', '555', '9999'), ('212', '555', '0000')].

'''


'''






https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/

mkvirtualenv -p python3.8 <environment name>
workon <virtualenv-name>.



/home/matrixbox/my_site2024
ecomprj
myenv


Virtualenv
Code



--------------
django-taggit==3.0.0
django-theme-material-kit==1.0.19
Pillow==10.1.0
Django==4.2.2
crispy-bootstrap5==0.7
django-ckeditor-5==0.2.10
django-ckeditor==6.0.0
paypal-payouts-sdk==1.0.0
paypalhttp==1.0.1
django-paypal==2.0
stripe==7.0.0

shortuuid==1.0.11


单击右键-填充-内容识别


'''

#  THIS ONE IS GOOD!!!!
import pyperclip
import re

def extract_image_references_from_clipboard():
    '''Django helper: From clipboard html code extract all src attribute'''
    # Get HTML content from the clipboard
    html_content = pyperclip.paste()

    # Define a regex pattern to match image URLs in any attribute
    pattern = r'[\w-]+="([^"]+\.(?:jpg|jpeg|png|gif|ico|svg|bmp))"'

    # Find all matches for the pattern
    matches = re.findall(pattern, html_content, re.IGNORECASE)

    # Print the extracted image references
    print("Extracted image references:")
    for img in matches:
        print(img)




def modify_image_references_from_clipboard(modify_func):
    '''Django helper: modify all img src attribute, with some function to static format'''
    # Get HTML content from the clipboard
    html_content = pyperclip.paste()

    # Define a regex pattern to match image URLs in any attribute
    pattern = r'''(href|src|data-[\w-]+)=["']([^"]+\.(?:jpg|jpeg|png|gif|ico|svg|bmp))["']'''

    # Define the replacement function to be used with re.sub
    def replacement(match):
        attribute = match.group(1)
        img_reference = match.group(2)
        new_reference = modify_func(img_reference)
        return f'{attribute}="{new_reference}"'

    # Use re.sub to replace the pattern with the modified references
    modified_html_content = re.sub(pattern, replacement, html_content, flags=re.IGNORECASE)

    # Print or copy the modified content back to the clipboard
    pyperclip.copy(modified_html_content)
    print(modified_html_content)


 
def prefix_static(prefix):
    ''' usage: modify_image_references_from_clipboard(prefix_static("fuck/"))'''
    def modify(img_reference):
        new_reference = prefix + img_reference
        result = f"{{% static \'{new_reference}\' %}}"
        return result
    return modify    

modify_image_references_from_clipboard(prefix_static("shop/")




n = lambda input_path: [folder for folder in os.listdir(input_path)] # dirs and files names
n = lambda input_path: [file for file in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, file))] # files names
n = lambda input_path: [folder for folder in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, folder))] # dirs names

p = lambda input_path: [os.path.join(input_path, folder) for folder in os.listdir(input_path)] # dirs and files paths
p = lambda input_path: [os.path.join(input_path, folder) for folder in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, folder))] # files paths
p = lambda input_path: [os.path.join(input_path, folder) for folder in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, folder))] # dirs paths

template_names = [
    'about-us.html',
    'blog-single-post.html',
    'blog.html',
    'checkout.html',
    'contacts.html',
    'index.html',
    'privacy.html',
    'search-results.html',
    'shop.html',
    'single-product.html'
]

import pyperclip as p

def generate_view_functions(template_names):
    view_functions = []

    for template in template_names:
        view_name = template.replace('.html', '').replace('-', '_')
        function_definition = f"""
def {view_name}(request):
    return render(request, 'core/{template}')
"""
        view_functions.append(function_definition)

    # Join all function definitions into a single string
    views_code = "\n".join(view_functions)
    p.copy(views_code)

def generate_url_patterns(template_names):
    url_patterns = []

    for template in template_names:
        view_name = template.replace('.html', '').replace('-', '_')
        url_pattern = template.replace('.html', '').replace('_', '-')
        url_pattern_line = f"path('{url_pattern}/', views.{view_name}, name='{view_name}'),"
        url_patterns.append(url_pattern_line)

    # Join all URL patterns into a single string
    urls_code = "\n".join(url_patterns)
    p.copy(urls_code)























# modify_image_references_from_clipboard(prefix_static("fuck/"))



def modify_customized_references_from_clipboard(modify_func):
    # Get HTML content from the clipboard
    html_content = pyperclip.paste()

    # Define a regex pattern to match image URLs in any attribute
    pattern = r'(href|action)="([^"]+\.(?:html))"'

    # Define the replacement function to be used with re.sub
    def replacement(match):
        attribute = match.group(1)
        img_reference = match.group(2)
        new_reference = modify_func(img_reference.replace(".html","").replace("-","_"))
        return f'{attribute}="{{% url \'{new_reference}\' %}}"'

    # Use re.sub to replace the pattern with the modified references
    modified_html_content = re.sub(pattern, replacement, html_content, flags=re.IGNORECASE)

    # Print or copy the modified content back to the clipboard
    pyperclip.copy(modified_html_content)
    print(modified_html_content)


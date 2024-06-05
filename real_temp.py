import random
import pyinputplus as pyip


def simulate_monty_hall(n_simulations):
    switch_wins  =0
    stay_wins = 0

    for _ in range(n_simulations):
        prize_door = random.randint(0, 2)

        initial_choice = random.randint(0, 2)

        remaining_doors = [door for door in range(3) if door != initial_choice and door != prize_door]
        door_opened_by_host = random.choice(remaining_doors)

        switch_choice = next(d for d in range(3) for d != initial_choice and d != door_opened_by_host)

        




def modify_image_references_from_clipboard1(modify_func):
    # Get HTML content from the clipboard
    html_content = pyperclip.paste()

    # Define a regex pattern to match image URLs in any attribute
    pattern = r'(src|data-[\w-]+)="([^"]+\.(?:jpg|jpeg|png|gif|ico|svg|bmp))"'

    # Define the replacement function to be used with re.sub
    def replacement(match):
        attribute = match.group(1)
        img_reference = match.group(2)
        new_reference = modify_func(img_reference)
        return f'{attribute}="{{% static \'{new_reference}\' %}}"'

    # Use re.sub to replace the pattern with the modified references
    modified_html_content = re.sub(pattern, replacement, html_content, flags=re.IGNORECASE)

    # Print or copy the modified content back to the clipboard
    pyperclip.copy(modified_html_content)
    print(modified_html_content)


def modify_image_references_from_clipboard2(modify_func):
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




def some_function(prefix):
    def modify(img_reference):
        return prefix + img_reference
    return modify

modify_image_references_from_clipboard1(some_function("core/"))
modify_image_references_from_clipboard2(some_function("core:"))


import pyperclip
import re

def add_prefix_to_classes(html, prefix):
    # Regular expression to find all class attributes
    class_pattern = re.compile(r'class="([^"]*)"')

    def repl(match):
        # Extract the class names
        classes = match.group(1)
        # Split the class names into a list
        class_list = classes.split()
        # Add the prefix to each class name
        prefixed_classes = [prefix + class_name for class_name in class_list]
        # Join the class names back into a single string
        return f'class="{" ".join(prefixed_classes)}"'

    # Substitute all class attributes in the HTML with the prefixed class names
    modified_html = class_pattern.sub(repl, html)
    return modified_html

# Read HTML from the clipboard
html = pyperclip.paste()

# Define the prefix
prefix = "prefix-"

# Add the prefix to all class names
modified_html = add_prefix_to_classes(html, prefix)

# Write the modified HTML back to the clipboard
pyperclip.copy(modified_html)

print("The HTML code with prefixed class names has been copied to the clipboard.")



def find_classes_from_clipboard():
    # Regular expression to find all class attributes
    import pyperclip as p
    class_pattern = re.compile(r'class="([^"]*)"')
    html = p.paste()
    class_list = class_pattern.findall(html)
    # print(class_list)
    class_list_final = []
    for i in class_list:
        sub_lt = i.split(" ")
        for slt in sub_lt:
            if slt not in class_list_final:
                class_list_final.append(slt)
    print(class_list_final)
    for i in class_list_final:
        print(i)





from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


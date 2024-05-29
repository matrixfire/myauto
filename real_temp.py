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

        


#  THIS ONE IS GOOD!!!!
import pyperclip
import re

def extract_image_references_from_clipboard():
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

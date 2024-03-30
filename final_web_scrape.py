'''
1, Always call raise_for_status() after calling requests.get(). You want to be sure that the download has actually worked before your program continues.
2, Beautiful Soup’s select() or Selenium’s find_element_by_css_selector() methods
3, 
Multiple Element Selector (a, b): Selects all <a> and <b> elements.


Descendant Selector (a b): Selects all <b> elements that are descendants of <a> elements.

Child Selector (a > b): Selects all <b> elements where the parent is an <a> element.

Adjacent Sibling Selector (a + b): Selects the first <b> element that immediately follows an <a> element.

Attribute Selector ([a=b]): Selects all elements with an attribute a equal to b.

Pseudoclass Selector (a:b): Selects all elements that are in the state :b of the element <a>.

Pseudoelement Selector (a::b): Selects all ::b pseudoelements on element <a>.


4,
Sure, here's a summary:

- `soup.select('input[name]')`: This command is used to find and select all `<input>` elements that have a `name` attribute, regardless of the value of the `name` attribute.

- `soup.select('input[type="button"]')`: This one is used to find and select all `<input>` elements that specifically have a `type` attribute set to the value `"button"`.

'''


import requests
from bs4 import BeautifulSoup

def save_file_from_url(url, filename):
    try:
        # Fetch the content from the URL
        res = requests.get(url)
        res.raise_for_status()

        # Open a file for writing in binary mode
        with open(filename, 'wb') as file: # wb
            # Write the content in chunks
            for chunk in res.iter_content(100_000):
                file.write(chunk)
        print("File saved successfully as", filename)
    except Exception as e:
        print("Error occurred:", e)

# Example usage:
save_file_from_url('https://automatetheboringstuff.com/files/rj.txt', 'RomeoAndJuliet2.txt')




def parse_html_and_select(selector, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    elems = soup.select(selector)
    
    elements_summary = []
    for elem in elems:
        elements_summary.append({
            'text': elem.getText(),
            'attributes': elem.attrs
        })
    
    summary = {
        'count': len(elems),
        'elements': elements_summary
    }
    
    return summary
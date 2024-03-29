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
'''


import requests

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

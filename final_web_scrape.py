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





5,
Your computer is like a big house.
A hypervisor is like a magical house manager who divides the house into separate apartments (virtual machines) for different families (operating systems) to live in independently.
Virtualization is the process of creating these separate, virtual apartments inside the big house.
The client refers to the end users or software that uses or manages these virtual apartments.


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



import requests
import os
import bs4
import random
import time

def save_image(image_url, directory='xkcd'):
    """Downloads and saves an image from a given URL to a specified directory."""
    print(f'Downloading image {image_url}...')
    response = requests.get(image_url)
    response.raise_for_status()
    # Save the image to the specified directory
    with open(os.path.join(directory, os.path.basename(image_url)), 'wb') as image_file:
        for chunk in response.iter_content(100_000):
            image_file.write(chunk)

def download_xkcd_comics():
    """Downloads all XKCD comics and saves them in a local directory."""
    url = 'https://xkcd.com'
    os.makedirs('xkcd', exist_ok=True)

    while not url.endswith('#'):
        print(f'Downloading page {url}...')
        response = requests.get(url)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        comic_element = soup.select('#comic img')
        if not comic_element:
            print('Could not find comic image.')
        else:
            comic_url = 'https:' + comic_element[0].get('src')
            save_image(comic_url)  # Call the save_image function

        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prev_link.get('href')

        time.sleep(random.randint(1, 3))
        if random.randint(1, 30) == 5:
            print('Lucky stop.')
            break

    print('Done.')

# Example usage:
# download_xkcd_comics()

# Example usage:
# download_xkcd_comics()


'''
https://blog.csdn.net/qq_43125235/article/details/125601564


import time
# 导入selenium包
from selenium import webdriver
from selenium.webdriver.common.by import By
# 启动并打开指定页面
browser = webdriver.Firefox()
browser.get("http://www.baidu.com/")
# 通过name属性选择文本框元素，并设置内容
browser.find_element(By.NAME,'wd').send_keys("selenium")
# 通过通过ID属性获取“百度一下”按钮，并执行点击操作
browser.find_element(By.ID,"su").click()
# 停留五秒后关闭浏览器
time.sleep(5)
browser.quit()

.send_keys('XXX')
.clear()
.submit()
.click()

title页面标题
page_source 页面源码
current_url页面连接
text标签内文本


browser.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys('selenium')

browser.implicitly_wait(5)

maximize_window()窗口最大化。
minimize_window()窗口最小化。
set_window_size(width,height)调整窗口到指定尺寸。

forward()前进一页。
back()后退一页。
refresh()页面刷新


/*[@id="toolbar-search-input" and @yy='bb']/p

find_element()系列：用于定位单个的页面元素。
find_elements()系列：用于定位一组页面元素，获取到的是一组列表。

By.ID
By.NAME
By.CLASS_NAME
By.TAG_NAME
By.LINK_TEXT
By.PARTIAL_LINK_TEXT
By.XPATH
By.CSS_SELECTOR

current_window_handle
window_handles
switch_to.window("XX")
switch_to.frame(XX)
switch_to.parent_frame()
switch_to.alert

'''
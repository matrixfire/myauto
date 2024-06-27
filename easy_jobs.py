import sys

# print(sys.argv)

import webbrowser

def open_links():
    links = [
        "https://chat.openai.com",
        "https://www.bing.com/chat",
        "https://yiyan.baidu.com/",
        "https://kimi.moonshot.cn/chat"
    ]
    for link in links:
        webbrowser.open(link)

# Call the function to open the links
open_links()
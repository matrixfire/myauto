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




https://blog.csdn.net/Everly_/article/details/133784236
'''




import os
import pickle
import time
from selenium import webdriver

# URLs
DAMAI_URL = "https://www.damai.cn/"
LOGIN_URL = "https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F"
TARGET_URL = 'https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.77f24d15RWgT4o&id=654534889506&clicktitle=%E5%A4%A7%E4%BC%97%E7'

class Concert:
    def __init__(self):
        self.status = 0  # 状态,表示如今进行到何种程度
        self.login_method = 1  # {0:模拟登录,1:Cookie登录}自行选择登录方式
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')  # 默认Chrome浏览器

    def set_cookie(self):
        self.driver.get(DAMAI_URL)
        print("###请点击登录###")
        while self.driver.title.find('大麦网-全球演出赛事官方购票平台') != -1:
            time.sleep(1)
        print('###请扫码登录###')

        while self.driver.title != '大麦网-全球演出赛事官方购票平台-100%正品、先付先抢、在线选座！':
            time.sleep(1)
        print("###扫码成功###")
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
        print("###Cookie保存成功###")
        self.driver.get(TARGET_URL)

    def get_cookie(self):
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))  # 载入cookie
            for cookie in cookies:
                cookie_dict = {
                    'domain': '.damai.cn',  # 必须有，不然就是假登录
                    'name': cookie.get('name'),
                    'value': cookie.get('value')
                }
                self.driver.add_cookie(cookie_dict)
            print('###载入Cookie###')
        except Exception as e:
            print(e)

    def login(self):
        if self.login_method == 0:
            self.driver.get(LOGIN_URL)
            print('###开始登录###')
        elif self.login_method == 1:
            if not os.path.exists('cookies.pkl'):
                self.set_cookie()
            else:
                self.driver.get(TARGET_URL)
                self.get_cookie()

    def enter_concert(self):
        print('###打开浏览器，进入大麦网###')
        self.login()
        self.driver.refresh()
        self.status = 2
        print("###登录成功###")

    def isElementExist(self, element):
        try:
            self.driver.find_element_by_xpath(element)
            return True
        except:
            return False

    def choose_ticket(self):
        if self.status == 2:  # If logged in successfully
            print("="*30)
            print("###开始进行日期及票价选择###")
            while self.driver.title.find('确认订单') == -1:
                try:
                    buybutton = self.driver.find_element_by_class_name('buybtn').text
                    if buybutton == "提交缺货登记":
                        self.status = 2
                        self.driver.get(TARGET_URL)
                        print('###抢票未开始，刷新等待开始###')
                        continue
                    elif buybutton == "立即预定":
                        self.driver.find_element_by_class_name('buybtn').click()
                        self.status = 3  # Status updated to 'ticket selecting'
                    elif buybutton == "立即购买":
                        self.driver.find_element_by_class_name('buybtn').click()
                        self.status = 4  # Status updated to 'purchasing'
                    elif buybutton == "选座购买":
                        self.driver.find_element_by_class_name('buybtn').click()
                        self.status = 5  # Status updated to 'seat selecting'
                except Exception as e:
                    print('###未跳转到订单结算界面###', e)
                title = self.driver.title
                if title == '选座购买':
                    self.choice_seats()  # Call choice_seats if it's time to select seats
                elif title == '确认订单':
                    self.check_order()  # Check order when ready
                    break


    def choice_seats(self):
        print('###请进行座位选择###')
        while self.driver.title == '选座购买':
            while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/img'):
                # Assuming the existence of the image indicates seats have not yet been selected
                print('请快速的选择您的座位！！！')
            # Once seats are selected, confirm the selection
            while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[2]/div'):
                # Assuming this element exists when it's time to confirm seat selection
                self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/button').click()
                break  # Exit the loop after confirming seat selection

    def check_order(self):
        if self.status in [3, 4, 5]:  # If at the stage of confirming order
            print('###开始确认订单###')
            try:
                # Select the first ticket buyer by default or apply any necessary configurations
                self.driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/div[1]/div/label').click()
            except Exception as e:
                print("###购票人信息选中失败，自行查看元素位置###", e)
            # Final step to submit the order
            time.sleep(0.5)  # Wait a bit for page elements to load properly
            self.driver.find_element_by_xpath('//div[@class = "w1200"]//div[2]//div//div[9]//button[1]').click()

    def finish(self):
        self.driver.quit()

if __name__ == '__main__':
    try:
        con = Concert()
        con.enter_concert()
        con.choose_ticket()
    except Exception as e:
        print(e)
        con.finish()

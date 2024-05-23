# import time
# import csv
# import pyinputplus as pyip
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Initialize the WebDriver (e.g., for Firefox)
# driver = webdriver.Firefox()

# # Navigate to the desired webpage
# driver.get('https://ideas.lego.com/')  # Replace with the actual URL

# time.sleep(5)  # Adjust the sleep time if necessary

# # Scroll down to load more images (adjust the number of scrolls as needed)
# for _ in range(3):  # Can be changed
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)  # Adjust the sleep time if necessary

# # Locate the cards holder element
# cards_holder = driver.find_element(By.XPATH, '//*[@id="whats-up-app"]/div[2]/div[1]/div/div[2]')

# # Locate all card elements within the cards holder
# cards = cards_holder.find_elements(By.XPATH, './/div[@data-test="project-tile"]')

# # List to hold all extracted data
# data = []

# # Iterate through each card and extract the required information
# for card in cards[:]:
#     # 1. Get the image URL
#     img_element = card.find_element(By.XPATH, './/img[@data-test="card-image"]')
#     img_url = img_element.get_attribute('src')

#     # 2. Get the title
#     title_element = card.find_element(By.XPATH, './/h3[@data-test="card-title"]/a')
#     title = title_element.text

#     # 3. Get the author's name
#     author_element = card.find_element(By.XPATH, './/div[@class="user-alias text-truncate"]/a')
#     author = author_element.text

#     # 4. Get the release date
#     date_element = card.find_element(By.XPATH, './/div[@class="card-published"]/time')
#     release_date = date_element.get_attribute('title')

#     # 5. Get the number of supporters
#     supporters_element = card.find_element(By.XPATH, './/a[@data-test="project-support-value"]')
#     supporters = supporters_element.text

#     # 6. Construct the detailed page URL
#     detailed_page_url = title_element.get_attribute('href')

#     # Append the extracted information to the data list
#     data.append([img_url, title, author, release_date, supporters, detailed_page_url])

#     # Optionally print the extracted information
#     print(f"Image URL: {img_url}")
#     print(f"Title: {title}")
#     print(f"Author: {author}")
#     print(f"Release Date: {release_date}")
#     print(f"Supporters: {supporters}")
#     print(f"Detailed Page URL: {detailed_page_url}")
#     print("="*50)

# # Optionally, close the WebDriver
# driver.quit()

# # Prompt for the CSV file name with a default option
# csv_filename = pyip.inputStr(prompt="Enter the CSV file name (default is 'lego_imgs.csv'): ", default='lego_imgs.csv')

# # Write the data to a CSV file
# with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     # Write the header
#     writer.writerow(['Image URL', 'Title', 'Author', 'Release Date', 'Supporters', 'Detailed Page URL'])
#     # Write the data
#     writer.writerows(data)

# print(f"Data successfully written to {csv_filename}")



import time
import random
import sys
import pyinputplus as pyip
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

def collect_lego_data():
    # Initialize the WebDriver (e.g., for Firefox)
    driver = webdriver.Firefox()

    # Navigate to the desired webpage
    driver.get('https://ideas.lego.com/')  # Replace with the actual URL

    time.sleep(5)  # Adjust the sleep time if necessary

    # Initialize a set to keep track of seen project URLs
    seen_urls = set()

    # List to hold all extracted data
    data = []

    # Scroll down to load more images
    for _ in range(20):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2 * random.random())
    time.sleep(2+ random.randint(3, 10))  # Adjust the sleep time if necessary

    # Locate the cards holder element
    cards_holder = driver.find_element(By.XPATH, '//*[@id="whats-up-app"]/div[2]/div[1]/div/div[2]')

    # Locate all card elements within the cards holder
    cards = cards_holder.find_elements(By.XPATH, './/div[@data-test="project-tile"]')

    for card in cards:
        # 1. Get the image URL
        img_element = card.find_element(By.XPATH, './/img[@data-test="card-image"]')
        img_url = img_element.get_attribute('src')

        # 2. Get the title
        title_element = card.find_element(By.XPATH, './/h3[@data-test="card-title"]/a')
        title = title_element.text

        # 3. Get the author's name
        author_element = card.find_element(By.XPATH, './/div[@class="user-alias text-truncate"]/a')
        author = author_element.text

        # 4. Get the release date
        date_element = card.find_element(By.XPATH, './/div[@class="card-published"]/time')
        release_date = date_element.get_attribute('title')

        # 5. Get the number of supporters
        supporters_element = card.find_element(By.XPATH, './/a[@data-test="project-support-value"]')
        supporters = supporters_element.text

        # 6. Construct the detailed page URL
        detailed_page_url = title_element.get_attribute('href')

        # Check if this URL has already been processed
        if detailed_page_url in seen_urls:
            print("Found duplicate.")
            continue

        # Add the URL to the seen set
        seen_urls.add(detailed_page_url)

        # Append the extracted information to the data list
        data.append([img_url, title, author, release_date, supporters, detailed_page_url])

        # Optionally print the extracted information
        print(f"Image URL: {img_url}")
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Release Date: {release_date}")
        print(f"Supporters: {supporters}")
        print(f"Detailed Page URL: {detailed_page_url}")
        print("="*50)

    # Optionally, close the WebDriver
    driver.quit()

    # Prompt for the Excel file name with a default option
    excel_filename = pyip.inputStr(prompt="Enter the Excel file name (default is 'lego_imgs.xlsx'): ", default='lego_imgs.xlsx')

    # Create an Excel workbook and worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Lego Ideas Data'

    # Write the header
    headers = ['Image URL', 'Title', 'Author', 'Release Date', 'Supporters', 'Detailed Page URL']
    sheet.append(headers)

    # Write the data
    for row in data:
        sheet.append(row)

    # Save the workbook
    workbook.save(excel_filename)
    print(f"Data successfully written to {excel_filename}")

if __name__ == "__main__":
    collect_lego_data()

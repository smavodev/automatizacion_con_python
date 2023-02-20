from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = 'https://www.thesun.co.uk/sport/football/'
path = '/Users/Desktop/Web Scraping/Automatizacion_con_Python/Driver/chromedriver'  # introduce path here

# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(website)

# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

image = []
titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='./a/h3').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('football.csv')

driver.quit()

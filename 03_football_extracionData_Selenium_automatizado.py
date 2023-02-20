from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

# Preparing script before we convert it to executable
application_path = os.path.dirname(sys.executable)

# get date in format MMDDYYYY
now = datetime.now()
datetime_now = now.strftime("%m%d%Y_%H%M%S")  # %m%d%Y %H:%M:%S

website = 'https://www.thesun.co.uk/sport/football/'
path = '/Users/Desktop/Web Scraping/Automatizacion_con_Python/Driver/chromedriver'  # introduce path here

# Headless mode
options = Options()
options.headless = True
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(website)

containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

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

# Exporting data to the same folder where the executable will be located
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'football_{datetime_now}.csv'
final_path = os.path.join(application_path, file_name)  # .join "Permite unir rutas"
df_headlines.to_csv(final_path)
# print(final_path)
driver.quit()


# Ejecutarlo el instalador de la siguiente manera para crearlo
# pyinstaller --onefile 03_football_extracionData_Selenium_automatizado.py

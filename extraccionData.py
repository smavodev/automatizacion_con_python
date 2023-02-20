from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = 'https://www.thesun.co.uk/sport/football/'
path = '/Users/Desktop/Web Scraping/Automatizacion_con_Python/Driver/chromedriver'  # introduce path here

# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(website)



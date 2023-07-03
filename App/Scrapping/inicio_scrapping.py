from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import pandas as pd

driver_path = 'C:/Users/NickDev/Documents/Ayuda Diego/App/Scrapping/driver/chromedriver.exe'

# opciones para apertura del navegador.
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

start_driver = webdriver.Chrome(options=options)
start_driver.get('https://my.ecom.com.co/co/')

input('Ingreso a ecom, exitoso.')




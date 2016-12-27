# Written By: Gil Rael
# basspro_sales_notifier.py will notify Gil Rael via text message if item of interest
# is found on the basspro.com web site

# import required modules

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# this allows you to catch a thrown exception and add your own exception
# so your script continues to run and exits normally
from selenium.common.exceptions import NoSuchElementException
from twilio.rest import TwilioRestClient


# locate product of interest that is on sale at basspro.com and send
# ON SALE TODAY text message if item is on sale
# or send NO SALE TODAY text message if item of interest is not on sale

def locate_sale_item():
# open Firefox web browswer and maximize window
    driver = webdriver.Firefox()
    driver.maximize_window()
# open Caliberusa.com sales page
    driver.get("http://www.basspro.com/Ascend-D10-SitIn-Kayak-Purple/product/11081905012222/")
    driver.implicitly_wait(30)
    element = driver.find_element_by_class_name("sale")

    driver.quit()
locate_sale_item();

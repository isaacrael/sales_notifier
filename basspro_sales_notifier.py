# Written By: Gil Rael
# basspro_sales_notifier.py will notify Gil Rael via text message if item of interest
# is found on the basspro.com web site

# try and find ammo that is on sale to verify if your logic is correct for ammo sale items
# may need to eliminate the try and except class since it seems that the element is found
# but may not be displayed determine if class=sale can be found on the UMC 9mm page

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
# next two commented out lines are used to test a product that is on sale vs a product that is not on sale
#    driver.get("http://www.basspro.com/Ascend-D10-SitIn-Kayak-Purple/product/11081905012222/")
#    driver.get("http://www.basspro.com/RedHead-FireResistant-10Gun-Safe/product/1602111742/
    driver.get("http://www.basspro.com/Remington-UMC-Handgun-Ammo-Mega-Pack/product/53416/")
    driver.implicitly_wait(30)
    try:
        element = driver.find_element_by_class_name("sale")
        if element.is_displayed():
            client = TwilioRestClient("AC2c8bb5d4f471c5ccf25765e4f757b030", "5183d8a42f3d1a9084a4325029132058")
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
            client.messages.create(to="+15058330785", from_="+15057966457",

                       body="Hello from Pi!.....ON SALE TODAY! : ) Time To Buy Basspro Remington UMC 9mm Ammo"
                            "http://www.basspro.com/Remington-UMC-Handgun-Ammo-Mega-Pack/product/53416/")
    except NoSuchElementException:
        print("Item Not On Sale....")
    driver.quit()
locate_sale_item();

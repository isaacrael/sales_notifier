# Written By: Gil Rael
# basspro_sales_notifier.py will notify Gil Rael via text message if item of interest
# is on sale on the basspro.com web site

# import required modules

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# this allows you to catch a thrown exception and add your own exception
# so your script continues to run and exits normally
from selenium.common.exceptions import NoSuchElementException
from twilio.rest import TwilioRestClient
# pyvirtualdisplay needs to be installed pip install pyvirtualdisplay in order to run this script from crontab
# on Raspberry Pi, also xvfb needs to be installed sudo apt-get install xvfb
from pyvirtualdisplay import Display


# locate product of interest that is on sale at basspro.com and send
# ON SALE TODAY text message if item is on sale


def locate_sale_item():
# pyvirtualdisplay is needed in order to run this script from cron define display and start display
# note uncomment the next two lines if you are going to run this script from cron if you run this
# script from the the command line python calibers_sales_notifier.py and the lines below are not commented
# out you will not see the firefox web brower open
#    display = Display(visible=0, size=(800, 600))
#    display.start()
# open Firefox web browswer and maximize window
    driver = webdriver.Firefox()
    driver.maximize_window()
# open basspro.com sales page
# next five commented out lines are used to test a product that is on sale vs a product that is not on sale
#    driver.get("http://www.basspro.com/Ascend-D10-SitIn-Kayak-Purple/product/11081905012222/")
#    driver.get("http://www.basspro.com/RedHead-FireResistant-10Gun-Safe/product/1602111742/
#    http://www.basspro.com/Remington-Premier-Golden-Saber-Centerfire-Handgun-Ammo/product/82328/
#    driver.get("http://www.basspro.com/Remington-UMC-Handgun-Ammo-Mega-Pack/product/53416/")
    driver.get("http://www.basspro.com/Remington-UMC-Handgun-Ammo-Mega-Pack/product/53416/")
    driver.implicitly_wait(30)
    element = driver.find_element_by_class_name("sale")
    if element.is_displayed():
        client = TwilioRestClient("AC2c8bb5d4f471c5ccf25765e4f757b030", "5183d8a42f3d1a9084a4325029132058")
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
        client.messages.create(to="+15058330785", from_="+15057966457",

                       body="Hello from Pi!.....ON SALE TODAY! : ) Time To Buy Basspro Remington UMC 9mm Ammo"
                           "http://www.basspro.com/Remington-UMC-Handgun-Ammo-Mega-Pack/product/53416/")
    else:
        client = TwilioRestClient("AC2c8bb5d4f471c5ccf25765e4f757b030", "5183d8a42f3d1a9084a4325029132058")
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
        client.messages.create(to="+15058330785", from_="+15057966457",

                       body="Hello from Pi!.....NO SALE TODAY AT BASSPRO! : (")
    driver.quit()
locate_sale_item();

# Written By: Gil Rael
# calibers_sales_notifier.py will notify Gil Rael via text message if item of interest
# is found on caliberusa.com sales page

# import required modules

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# NoSuchElementException allows you to catch a thrown exception and add your own exception
# so your script continues to run and exits normally
from selenium.common.exceptions import NoSuchElementException
from twilio.rest import TwilioRestClient
# pyvirtualdisplay needs to be installed pip install pyvirtualdisplay in order to run this script from crontab
# on Raspberry Pi, also xvfb needs to be installed sudo apt-get install xvfb
from pyvirtualdisplay import Display

# locate product of interest that is on sale at Calibers and send
# ON SALE TODAY text message if item is on sale
# or send NO SALE TODAY text message if item of interest is not on sale

def locate_sale_item():
#    print os.environ["PATH"]
# pyvirtualdisplay is needed in order to run this script from cron define display and start display
# note uncomment the next two lines if you are going to run this script from cron if you run this
# script from the the command line python calibers_sales_notifier.py and the lines below are not commented
# out you will not see the firefox web brower open
#    display = Display(visible=0, size=(800, 600))
#    display.start()
# open Firefox web browswer and maximize window
    driver = webdriver.Firefox("/usr/local/bin")
    driver.maximize_window()
# open Caliberusa.com sales page
    driver.get("https://www.calibersusa.com/all-products/browse/sale/yes/orderby/sort-by-sale/perpage/150")
    driver.implicitly_wait(30)
    try:
        elem = driver.find_element_by_partial_link_text('One Year Dual Membership')
        if elem.is_displayed():
            elem.click() # this will click the element if it is there
            client = TwilioRestClient("AC2c8bb5d4f471c5ccf25765e4f757b030", "5183d8a42f3d1a9084a4325029132058")
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
            client.messages.create(to="+15058330785", from_="+15057966457",

                       body="Hello from Pi!.....ON SALE TODAY! : ) Time To Buy Calibers One Year Dual Membership")
    except NoSuchElementException:
        client = TwilioRestClient("AC2c8bb5d4f471c5ccf25765e4f757b030", "5183d8a42f3d1a9084a4325029132058")
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
        client.messages.create(to="+15058330785", from_="+15057966457",

                    body="Hello from Pi!..NO SALE TODAY          : (  On Calibers One Year Dual Membership")
    driver.quit()
locate_sale_item();

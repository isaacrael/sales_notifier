# import required modules

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from twilio.rest import TwilioRestClient


# locate product of interest that is on sale

def locate_sale_item():
    driver = webdriver.Firefox()
    driver.maximize_window()
# open Caliberusa.com sales page
    driver.get("https://www.calibersusa.com/all-products/browse/sale/yes/orderby/sort-by-sale/perpage/150")
    driver.implicitly_wait(15)
    link = driver.find_element_by_xpath('//a[@href="https://www.calibersusa.com/beretta/beretta-px4-magazine-40-sw-14rd-jm4px4014-430"]')
    print(link)
#https://www.calibersusa.com/beretta/beretta-px4-magazine-40-sw-14rd-jm4px4014-430
# if link exists send text message
    if link == "https://www.calibersusa.com/beretta/beretta-px4-magazine-40-sw-14rd-jm4px4014-430":
        client = TwilioRestClient("AC2c8bb5d4f471c5ccf25765e4f757b030", "5183d8a42f3d1a9084a4325029132058")
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
        client.messages.create(to="+15058330785", from_="+15057966457",

                       body="Hello from Python!.....Time To Buy Calibers One Year Dual Membership")

locate_sale_item();






"""

def send_text_message_via_twilio():

# we import the Twilio client from the dependency we just installed

	from twilio.rest import TwilioRestClient


# the following line needs your Twilio Account SID and Auth Token

	client = TwilioRestClient("AC2c8bb5d4f471c5ccf25765e4f757b030", "5183d8a42f3d1a9084a4325029132058")



# change the "from_" number to your Twilio number and the "to" number

# to the phone number you signed up for Twilio with, or upgrade your

# account to send SMS to any phone number

	client.messages.create(to="+15058330785", from_="+15057966457", 

                       body="Hello from Python!.....Time To Buy Calibers One Year Dual Membership")

send_text_message_via_twilio()

"""
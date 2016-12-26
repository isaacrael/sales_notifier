from selenium import webdriver
driver = webdriver.Firefox()
driver.maximize_window()
#driver.get("http://localhost:8080/")
driver.get("http://cnn.com/")

def send_text_message_via_twilio():

# we import the Twilio client from the dependency we just installed

	from twilio.rest import TwilioRestClient


# the following line needs your Twilio Account SID and Auth Token

	client = TwilioRestClient("AC2c8bb5d4f471c5ccf25765e4f757b030", "5183d8a42f3d1a9084a4325029132058")



# change the "from_" number to your Twilio number and the "to" number

# to the phone number you signed up for Twilio with, or upgrade your

# account to send SMS to any phone number

	client.messages.create(to="+15058330785", from_="+15057966457", 

                       body="Hello from Python!.....Time To Buy Calibers Membership")

send_text_message_via_twilio()

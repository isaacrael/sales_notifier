# Written By: Gil Rael
# neiman_marcus_sales_notifier.py will notify Gil Rael via text message if item(s) of interest
# are on sale on the neimanmarcus.com web site

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


# locate product of interest at neimanmarcus.com and send
# ON SALE TODAY text message if item is on sale or NO SALE TODAY message if item is not on sale


def locate_sale_item():
# pyvirtualdisplay is needed in order to run this script from cron define display and start display
# note uncomment the next two lines if you are going to run this script from cron if you run this
# script from the the command line python calibers_sales_notifier.py and the lines below are not commented
# out you will not see the firefox web brower open
#    display = Display(visible=0, size=(1200, 900))
#    display.start()
# open Firefox web browswer and maximize window
    driver = webdriver.Firefox("/usr/local/bin")
    driver.maximize_window()
# open neimanmarcus.com sales page
# commented out lines below are used to test a product that is on sale vs a product that is not on sale


#    driver.get("http://www.neimanmarcus.com/Lalique-Crystal-Pour-Homme-Le-Lion-Eau-de-Parfum-Buddha/prod155230066_cat46510751__/p.prod?icid=&searchType=EndecaDrivenCat&rte=%252Fcategory.service%253FitemId%253Dcat46510751%2526pageSize%253D30%2526No%253D0%2526Ns%253DPCS_SORT%2526refinements%253D4294847645&eItemId=prod155230066&cmCat=product")
#    driver.get("http://www.neimanmarcus.com/Brioni-Patchwork-Sport-Shirt-Navy-The-Man-s-Store/prod190480449_cat62330756__/p.prod?icid=&searchType=EndecaDrivenCat&rte=%252Fcategory.jsp%253FitemId%253Dcat62330756%2526pageSize%253D30%2526No%253D0%2526refinements%253D&eItemId=prod190480449&cmCat=product")
    driver.get("https://www.neimanmarcus.com/David-Yurman/Mens/Rings/cat10440736_cat700731_cat540734/c.cat#userConstrainedResults=true&refinements=&page=1&pageSize=120&sort=&definitionPath=/nm/commerce/pagedef_rwd/template/EndecaDrivenHome&locationInput=&radiusInput=100&onlineOnly=&allStoresInput=false&rwd=true&catalogId=cat10440736&selectedRecentSize=&activeFavoriteSizesCount=0&activeInteraction=true")
    driver.implicitly_wait(30)
    try:
        element = driver.find_element_by_class_name("price-adornments-elim-suites")
        if element.is_enabled():
            client = TwilioRestClient("AC2c8bb5d4f471c5ccf25765e4f757b030", "5183d8a42f3d1a9084a4325029132058")
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
            client.messages.create(to="+15058330785", from_="+15057966457",

                       body="Hello from Pi!.....ON SALE TODAY DAVID YURMAN AT NEIMAN MARCUS! : ) Time To Buy ......"
                           "https://www.neimanmarcus.com/David-Yurman/Mens/Rings/cat10440736_cat700731_cat540734/c.cat#userConstrainedResults=true&refinements=&page=1&pageSize=120&sort=&definitionPath=/nm/commerce/pagedef_rwd/template/EndecaDrivenHome&locationInput=&radiusInput=100&onlineOnly=&allStoresInput=false&rwd=true&catalogId=cat10440736&selectedRecentSize=&activeFavoriteSizesCount=0&activeInteraction=true")
    except NoSuchElementException:
        client = TwilioRestClient("AC2c8bb5d4f471c5ccf25765e4f757b030", "5183d8a42f3d1a9084a4325029132058")
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
        client.messages.create(to="+15058330785", from_="+15057966457",

                       body="Hello from Pi!.....NO SALE TODAY DAVID YURMAN AT NEIMAN MARCUS! : (")
    driver.quit()
locate_sale_item();

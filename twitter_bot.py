# ---------------------****************************************************************************---------------- #
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# ---------------------------------********Importing******Packages*******----------------------------------------- #

PROMISED_UP = 10
PROMISED_DOWN = 200
TWITTER_EMAIL = ""
TWITTER_PW = ""

URL = "https://www.speedtest.net/"
Chrome_Driver_Path ="/Users/madisonavemoe/Desktop/Development/chromedriver"

# ------------------------------------------******SETTING***CONSTANTS******------------------------------------------ #


# ----------*****{CLASS CREATION--Initialized--web-driver-via-class-object-and-added-methods-&-attributes}*****------ #

class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(URL)
        time.sleep(2)
        self.driver.find_element_by_css_selector(".start-button a").click()
        time.sleep(45)
        self.down = self.driver.find_element_by_class_name("download-speed").text
        self.up = self.driver.find_element_by_class_name("upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(4)
        self.driver.find_element_by_css_selector("div>span[role*='button']").click()
        time.sleep(4)
        self.driver.find_element_by_css_selector("a[href='/login']").click()
        time.sleep(5)
        email = self.driver.find_element_by_css_selector("div>input[name='username']")
        email.send_keys("{USERNAME}")
        email.send_keys(Keys.ENTER)
        time.sleep(3)
        pass_w = self.driver.find_element_by_css_selector("div>input[name='password']")
        pass_w.send_keys("{YOURPW}")
        pass_w.send_keys(Keys.ENTER)
        time.sleep(5)
        message = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        message.send_keys(f"Hi @provider my current download speeds are {self.down} mbps and my current upload speeds are {self.up} mbps. "
                          f"You guaranteed me download speeds of {PROMISED_DOWN} mbps and upload of {PROMISED_UP}.Dont mind this post im just doing some automation tasks.")
        #tweet_button = self.driver.find_element_by_css_selector("div[data-testid='tweetButtonInline']").click()


x = InternetSpeedTwitterBot(Chrome_Driver_Path)
x.get_internet_speed()
print(x.down,x.up)
if int(float(x.up))< PROMISED_UP or int(float(x.down))<PROMISED_DOWN:
    x.tweet_at_provider()
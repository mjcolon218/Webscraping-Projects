from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
import time
CHROME_DRIVER_PATH = "/Users/madisonavemoe/Desktop/Development/chromedriver"


URL = "https://www.instagram.com/"
USER_NAME = ""
PASSWORD = ""



class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def login(self):
        self.driver.get(URL)
        time.sleep(4)
        username = self.driver.find_element_by_css_selector("input[name='username']")
        username.send_keys(USER_NAME)
        pass_w = self.driver.find_element_by_css_selector("input[name='password']")
        pass_w.send_keys(PASSWORD)
        time.sleep(2)
        pass_w.send_keys(Keys.ENTER)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".cmbtv"))).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.HoLwm'))).click()
        time.sleep(4)

    def find_followers(self,find_ig_name):
        find_followers = self.driver.get(f"https://www.instagram.com/{find_ig_name}")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        number_followers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text

        print(number_followers)
        pop_up_window = WebDriverWait(self.driver, 1).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'isgrP')))

        for _ in range(25):#This is how you scroll down to get the whole list of followers
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].scrollHeight',
            pop_up_window)
            time.sleep(1)
            print("Scroll_Successful")

        else:
            print("Issue  arrived")





    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
                print("followed")
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()





follower_bot = InstaFollower()
follower_bot.login()
follower_bot.find_followers("iceberg_flacko")
follower_bot.follow()


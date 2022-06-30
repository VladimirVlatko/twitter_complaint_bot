from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = YOUR PROMISED DOWNLOAD SPEED
PROMISED_UP = YOUR PROMISED UPLOAD SPEED
TWITTER_EMAIL = YOUR TWITTER EMAIL
TWITTER_PASS = YOUR TWITTER PASSWORD 
CHROME_DRIVER_PATH = YOUR CHROMEDRIVER PATH


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.down = 0
        self.up = 0

    #Check the download/upload speed on the speedtest website
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element(By.XPATH,
                                             "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div["
                                             "1]/a")
        go_button.click()

        time.sleep(60)

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                       '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div['
                                                       '2]/span').text

        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                           '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    # Login to twitter account and tweet the message with down/up speeds
    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com/login/")
        time.sleep(5)
        username = self.driver.find_element(By.XPATH,
                                            "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                            "2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        username.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH,
                                               "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                               "2]/div[2]/div/div/div/div[6]/div")
        next_button.click()
        time.sleep(3)
        password = self.driver.find_element(By.XPATH,
                                            "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                            "2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        new_tweet = self.driver.find_element(By.XPATH,
                                             "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
        new_tweet.click()
        time.sleep(3)

        tweet_text = self.driver.find_element(By.XPATH,
                                              "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div["
                                              "2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div["
                                              "1]/div/div/div/div/div/div/div/div/div/label/div["
                                              "1]/div/div/div/div/div[2]/div")
        tweet_text.send_keys(f"Hey {YOUR PROVIDER TWITTER USERNAME}, why is my internet speed {self.down} down/{self.up} up when I "
                             f"pay for {PROMISED_DOWN} down/{PROMISED_UP}")
        tweet_button = self.driver.find_element(By.XPATH,
                                                "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div["
                                                "2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div["
                                                "3]/div/div/div[2]/div[4]")
        tweet_button.click()

# Create bot
twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

twitter_bot.get_internet_speed()
time.sleep(1)
twitter_bot.tweet_at_provider()

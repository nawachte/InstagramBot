from selenium import webdriver
import time
import random
from urllib.request import urlretrieve

class RedditInstaBot:
    def __init__ (self):
        # self.username = username
        # self.password = password
        self.base_url = 'https://www.reddit.com'
        self.driver = webdriver.Chrome('./chromedriver')
        # self.login()
        self.usedSRC = {}
        self.suffixes = {}

    # def login(self):
    #     self.driver.get('{}/login/'.format(self.base_url))
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element_by_name('username').send_keys(self.username)
    #     self.driver.find_element_by_name('password').send_keys(self.password)
    #     self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
    #     time.sleep(4)

    def go_to_page(self,pageName):
        self.driver.get('{}/r/{}/top/?t=day'.format(self.base_url,pageName))
        time.sleep(2)

    def generateFileName(self):
        suffix = random.randint(0,10000000)
        while suffix in self.suffixes:
            suffix = random.randint(0, 10000000)
        self.suffixes[suffix]:0
        return 'meme'+str(suffix)

    def download_image_at(self,pageName):
        self.go_to_page(pageName)
        image = self.driver.find_elements_by_tag_name('img')[2]
        src = image.get_attribute('src')
        idx = 3
        while 'redditstatic' in src or 'redditmedia' in src or src in self.usedSRC.keys():
            image = self.driver.find_elements_by_tag_name('img')[2]
            src = image.get_attribute('src')
            idx += 1
        fileName = self.generateFileName()
        urlretrieve(src, 'memes/{}'.format(fileName))
        self.usedSRC.update({src,0})
        return fileName

    def quit(self):
        self.driver.quit()

if __name__=='__main__':
    reddit_bot = RedditInstaBot()
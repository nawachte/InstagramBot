from selenium import webdriver
import time
from threading import Timer
import requests
class InstaBot:
    def __init__(self):
        '''
            [args]
            username: str [instagram username]
            password: str [instagram password]

            [attributes]
            driver: selenium web driver
            base_url: further links are appended on to search instagram

            login: calls login method to login to instagram
        '''
        self.username = 'krombopulos_memes'
        self.password = 'wee4woo5'
        self.base_url = 'https://www.instagram.com'
        self.req = requests.Session()

        # self.driver = webdriver.Chrome('./chromedriver')
        # self.mobile_emulation = {"deviceName": "Nexus 5"}
        # self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_experimental_option("mobileEmulation", self.mobile_emulation)
        # self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
        #                           desired_capabilities=self.chrome_options.to_capabilities())

        self.driver = self.mobile_emulation()
        self.login()

    def wait(self,waitTime,optionalMSG=""):
        print(optionalMSG," wait")
        timer = Timer(waitTime, self.doNothing)
        timer.start()
        startTime = time.time()
        tFromStart = 1
        curr = time.time()
        while timer.is_alive():
            if curr>(startTime+tFromStart):
                print(".",end=" ")
                tFromStart+=1
            else:
                curr = time.time()
        print(" ")
        print("done")

    def doNothing(self):
        pass

    def mobile_emulation(self):
        mobile_emulation = {"deviceName": "Pixel 2"}
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("mobileEmulation", mobile_emulation)
        return webdriver.Chrome(executable_path=r"./chromedriver", options=opts)

    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        # self.driver.implicitly_wait(5)
        self.wait(3)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
        self.wait(1)
        self.close_notification()

    def close_notification(self):
        try:
            self.wait(3)
            close_noti_btn = self.driver.find_elements_by_tag_name('button')[1].click()
            # close_noti_btn = self.find_button('Not Now')
            # close_noti_btn.click()
            self.wait(1)
        except:
            print("no Not Now button")
            pass
        try:
            print("try cancel button")
            self.wait(6)
            self.driver.find_elements_by_xpath("//button[contains(text(), 'Cancel')]")[0].click()
            # close_noti_btn = self.driver.find_elements_by_tag_name('button')[3].click()
            # close_noti_btn = self.find_button('Cancel').click()
            self.wait(1)
        except:
            print("no Cancel button")
            pass
        print('Done with notifications')

    def find_button(self, buttonText):
        return self.driver.find_elements_by_xpath("//button[contains(text(), '{}')]".format(buttonText))
    def go_to_user(self,user):
        self.driver.get('{}/{}'.format(self.base_url,user))
        self.wait(4)

    def follow_user(self, user):
        self.go_to_user(user)
        followBtn = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        followBtn.click()
        self.wait(4)

    def unfollow_user(self, user):
        self.go_to_user(user)
        followingBtn = self.driver.find_elements_by_xpath("//button[contains(text(), 'Following')]")[0]
        followingBtn.click()
        self.wait(4)
        unfollowBtn = self.driver.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")
        unfollowBtn.click()
        self.wait(4)

    def append_username_file(self, user, numUsernames):
        usernamesFile = open("usernames.txt","a")
        self.wait(2)
        self.go_to_user(user)
        self.wait(5)
        followersLink = self.driver.find_element_by_css_selector('ul li a')
        followersLink.click()
        self.wait(3)
        usernames = self.driver.find_elements_by_tag_name('a')
        if (numUsernames<len(usernames)):
            numUsernames = len(usernames)
        printFlag = True
        for i in range(numUsernames):
            self.wait(.25)
            usrNmTxt = usernames[i].get_attribute('href')
            usrNmTxt = usrNmTxt[26:]
            usrNmTxt = usrNmTxt[:-1]
            if printFlag == True:
                usernamesFile.write("{}\n".format(usrNmTxt))
                print(usrNmTxt)
                printFlag = False
            else:
                printFlag = True
        usernamesFile.close()
    def quit(self):
        self.driver.quit()

# if __name__=='__main__':
#     # ig_bot = InstaBot('tempusername', 'temppassword')
#     ig_bot = InstaBot('krombopulos_memes', 'wee4woo5')
#     ig_bot.append_username_file('nando_valdiv',25)
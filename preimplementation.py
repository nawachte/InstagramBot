from selenium import webdriver
from threading import Timer
# import autoit
import requests
from InstaBot import InstaBot
image = 'memes/meme1.jpeg'
instaBot = InstaBot()
# file = {image: open()}
# file = open(image,'rb')
# values = {'upload_file':image,}
def postPhoto(fileName):
    print("start posting process")
    # element = instaBot.driver.find_element_by_css('div[class*="loadingWhiteBox"]')
    # instaBot.driver.execute_script("arguments[0].click();", element)
    print("clicking post button")
    post_btn = instaBot.driver.find_elements_by_xpath("//div[@role = 'menuitem']")[0].click().send_keys("memes/{}".format(fileName))
    # post_btn.send_keys("memes/{}".format(fileName))
    print("upload photo")
    response = instaBot.req.post(instaBot.base_url+'/upload/photo/')
    instaBot.wait(2)
    print("clicking expand")
    expand_button = instaBot.driver.find_elements_by_tag_name('button')[2].click()
    instaBot.wait(1)
    print("clicking next")
    next_button = instaBot.driver.find_elements_by_tag_name('button')[1].click()
    instaBot.wait(2)

postPhoto(image)


# from urllib.request import urlretrieve
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome('./chromedriver')
# driver.get('https://www.reddit.com/r/memes/top/?t=day')
# time.sleep(2)
# image = driver.find_elements_by_tag_name('img')[3]
# src = image.get_attribute('src')
# print(src)
# urlretrieve(src,'memes/test.png')
# driver.quit()


# image = driver.find_elements_by_tag_name('img')[i] (r/memes)
# i = 0|| https://styles.redditmedia.com/t5_2qjpg/styles/communityIcon_fhvk8lo7g2041.png
# i = 1|| https://www.redditstatic.com/gold/awards/icon/silver_32.png
# i = 2|| https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png
# i = 3|| https://preview.redd.it/m4vnb1c000141.jpg?width=640&crop=smart&auto=webp&s=aa4e816b6009f39e9ffd9c43353daf3524a43fd4
#         https://preview.redd.it/m4vnb1c000141.jpg?width=640&crop=smart&auto=webp&s=aa4e816b6009f39e9ffd9c43353daf3524a43fd4
#
# image = driver.find_elements_by_tag_name('img')[i] (r/dankmemes)
# i = 0|| https://styles.redditmedia.com/t5_2zmfe/styles/communityIcon_p1f98vyvwjx31.JPG
# i = 1|| https://www.redditstatic.com/gold/awards/icon/silver_32.png
# i = 2|| https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png
# i = 3|| https://i.redd.it/f58jl7yc52141.png
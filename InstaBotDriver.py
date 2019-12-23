from InstaBot import InstaBot
from RedditInstaBot import RedditInstaBot
from random import randint
from time import strftime,sleep
from queue_array import Queue
from DayInfo import DayInfo
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
from threading import Timer
import datetime

'''
monday is index 0 and goes through sunday at index 6
ex monday = post_time[0]
each day:
each day has a tuple
each tuple contains two times to randomly pick an hour from
-minutes will be randomly picked later
'''
post_time = [(11,16),(9,18),(10,15),(10,16),(9,16),(8,14),(9,14)]


'''
increase follow number and have a sleep period
    SLEEP PERIOD = 8 HOURS
(wait(minutes)/follow#) || (wait(minutes))

hour       minutes/number follow      post wait time
hour 0: (9/1)(7/1)(18/1)(4/1)(7/1)  ||(15)
hour 1: (10/2)(22/2)(8/1)(12/2)(4/1)||(4)
hour 2: (3/2)(19/1)(8/2)(12/2)      ||(19)
hour 3: (32/2)(4/3)(9/1)(7/1)       ||(8)
hour 4: (11/1)(11/2)(24/1)(7/2)     ||(7)
hour 5: (2/1)(12/1)(26/1)(6/1)(6/1) ||(8)
hour 6: (9/1)(4/2)(38/1)(3/2)       ||(6)
hour 7: (11/2)(17/1)(12/2)(11/2)    ||(20)
hour 8: (20/1)(8/1)(9/1)(14/2)      ||(7)

hour 9: (15/2)(10/2)(21/1)(8/1)     ||(6)
hour 10: (9/2)(14/1)(11/2)(8/1)     ||(18)

hour_list: idx[0] = number of people
        idx[1:] = (minutes/number follow)
'''
hour_list = [[5,(9,1),(7,1),(18,1),(4,1),(7,1),(20,0)]
    ,[6,(10,1),(22,2),(8,1),(12,2),(8,0)]
    ,[7,(3,2),(19,1),(8,2),(12,2),(19,0)]
    ,[7,(32,2),(4,3),(9,1),(7,1),(8,0)]
    ,[6,(11,1),(11,2),(24,1),(7,2),(7,0)]
    ,[5,(2,1),(12,1),(26,1),(6,1),(6,1),(8,0)]
    ,[6,(9,1),(4,2),(38,1),(3,2),(6,0)]
    ,[7,(11,2),(17,1),(12,2),(11,2),(20,0)]
    ,[5,(20,1),(8,1),(9,1),(14,2),(7,0)]
    ,[6,(15,2),(10,2),(21,1),(8,1),(6,0)]
    ,[6,(9,2),(14,1),(11,2),(8,1),(18,0)]]

DayInfo_queue = Queue()
global lines_read
lines_read = 0

def post_photo(fileName):
    pass

def getImages(numImages):
    #populate memes folder and create imageList
    imageNameList = []
    reddit_pages = ['me_irl','dankememes','memes']
    redditBot = RedditInstaBot
    images_to_get = numImages
    numFailures = 0
    while images_to_get>0:
        try:
            imageNameList.append(redditBot.download_image_at(reddit_pages[randint(0, len(reddit_pages)-1)]))
            images_to_get -= 1
        except:
            if numFailures>100:
                sendEmail('Image Error'
                          ,'The following error occurred while trying to upload an image:'
                          ,str(sys.exc_info()[0]))
            else:
                numFailures += 1
                pass
    return imageNameList


def setPostTimers(numPosts,imageFiles):
    sixtyMin = 60
    sixtySec = 60
    for i in range(numPosts):
        #get time interval
        timeInterval = post_time[datetime.datetime.today().weekday()]
        #convert time interval to hours to wait
        waitTime = (randint(timeInterval[0],timeInterval[1]))*sixtySec*sixtyMin
        #add on minutes
        waitTime += randint(0,59)*sixtySec
        #add on seconds
        waitTime += randint(0,59)
        timer = Timer(waitTime,post_photo,[imageFiles[i]])
        timer.start()


def unfollowPeople(numToUnfollow,user_list,numUnfollowed):
    instaBot = InstaBot()
    for i in range(numToUnfollow):
        user = user_list[i + numUnfollowed]
        instaBot.unfollow_user(user)
    instaBot.quit()

def setUnfollowTimers(hourList,userList):
    timeTotal = 0
    numToUnfollow = 0
    # for each hour that will users will be unfollowed
    for i in range(len(hourList)):
        for j in range(1, len(hourList[i])):
            parameters = [hourList[i][j][1], userList, numToUnfollow]
            timerLength = ((hourList[i][j][0] + timeTotal) * 60)+randint(0,59)
            timer = Timer(timerLength, unfollowPeople,parameters)
            timer.start()
            timeTotal += hourList[i][j][0]
            numToUnfollow += hourList[i][j][1]


def followPeople(numPeopleToFollow,user_list,numUsersFollowed):
    instaBot = InstaBot()
    for i in range(numPeopleToFollow):
        user = user_list[i+numUsersFollowed]
        instaBot.follow_user(user)
    instaBot.quit()
def setFollowTimers(hourList,user_list):
    timeTotal = 0
    numUsersFollowed = 0
    # for each hour in the hourlist
    for i in range(len(hourList)):
        # for every each user that will be followed this hour
        for j in range(1,len(hourList[i])):
            # set the timer for them to be followed
            parameters = [hourList[i][j][1],user_list,numUsersFollowed]
            timerLength = ((hourList[i][j][0]+timeTotal)*60)+randint(0,59)
            timer = Timer(timerLength,followPeople,parameters)
            timer.start()
            # increment the amount of time already set
            timeTotal += hourList[i][j][0]
            numUsersFollowed+=hourList[i][j][1]


def sendEmail(header,body,errormsg = ''):
    email = 'krombopulosm22@gmail.com'
    password = 'wee4woo5'
    recipient = 'nawachter50@gmail.com'
    subject = header
    message = body+'\n' + errormsg+"!!!Lines read: "+lines_read

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    txt = msg.as_string()
    server.sendmail(email, recipient, txt)
    server.quit()

def createDayInfo():
    global lines_read
    ###get hour list for the day###
    todays_hour_list = []
    user_total = 0
    #creates hour list
    for i in range(16):
        hour_stats = hour_list[randint(0,10)]
        user_total += hour_stats[0]
        todays_hour_list.append(hour_stats)
    ###get list of users for the day###
    user_list = []
    file = open('usernames.txt','r')
    #sets line pointer to where it left off
    for i in range(lines_read):
        file.readline()
    #creates userlist
    for i in range(user_total):
        #checks to make sure there is a next line
        try:
            user_list.append(file.readline())
            lines_read += 1
        except:
            sendEmail('File reading error','You are possibly out of users to parse.')
            break
    ###create followers day object and push it to the queue###
    numImages = randint(4,6)
    imageList = getImages(numImages)
    dayInfo = DayInfo(todays_hour_list,user_list,strftime("%m%d%Y"),numImages,imageList)
    DayInfo_queue.enqueue(dayInfo)
    return dayInfo


###MAIN LOOP###
try:
    start = False
    while True:
        current_hour = int(strftime("%H"))
        #start at 6am
        if current_hour == 6 and start == True:
            #create day information
            dayInfo = createDayInfo()
            #set timers for when to follow people
            setFollowTimers(dayInfo.hours_list,dayInfo.username_list)
            #if ready, set times to unfollow people
            if DayInfo_queue.peek().ready_for_unfollow():
                unfollowDayInfo = DayInfo_queue.dequeue()
                setUnfollowTimers(unfollowDayInfo.hours_list,unfollowDayInfo.username_list)
            #set timers to post photos
            setPostTimers(dayInfo.numImages,dayInfo.imageList)
            start = False
        if current_hour == 7:
            start = True
except:
    #send error email
    sendEmail('There has been an error','The following error has occured: ',str(sys.exc_info()))
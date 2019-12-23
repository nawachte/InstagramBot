from InstaBot import InstaBot


instaBot = InstaBot()
numPages = int(input("How many pages do you want to pull from? "))
userNames = input("Enter each username of these pages followed by a space. ")
while(userNames=="" or len(userNames.split(" "))!=numPages):
    print("Incorrect number of users")
    userNames = input("Enter each username with a space in between. ")
userNames = userNames.split(" ")
numUsers = int(input("How many users do you want to follow? "))
for i in range(numPages):
    numUsersPerPage = numUsers//numPages
    if i == numPages-1:
        total = numUsersPerPage*numPages
        if total<numUsers:
            numUsersPerPage += numUsers-total
    print("numUsersPerPage: ",numUsersPerPage)
    try:
        instaBot.append_username_file(userNames[i], numUsersPerPage)
    except:
        print("Error uploading usernames from user \"", userNames[i], "\"")
from time import strftime
class DayInfo:
    def __init__(self,hours_list,username_list,date,numImages,imageList):
        self.hours_list = hours_list
        self.username_list = username_list
        self.date = date
        self.unfollowDate = self.calcUFD(self.date)
        self.numImages = numImages
        self.imageList = imageList

    def calcUFD(self):
        dateList = list(self.date)
        month = int(self.date[:2])
        day = int(self.date[2:4])
        print('Month: ', month, ' Day: ', day)
        thirtyList = [4, 6, 9, 11]
        thirtyOneList = [1, 3, 5, 7, 8, 10, 12]
        if month == 2 and day <= 24 or (month in thirtyList) and day <= 26 or (
                month in thirtyOneList) and day <= 27:
            # just change day
            day += 4
            dateList[2] = str(day // 10)
            dateList[3] = str(day % 10)
        elif month < 12:
            if month in thirtyList:
                # change day
                remainder = (day + 4) - 30
                dateList[2] = '0'
                dateList[3] = str(remainder)
                # change month
            elif month in thirtyOneList:
                # change day
                remainder = (day + 4) - 31
                dateList[2] = '0'
                dateList[3] = str(remainder)
                # change month
                newMonth = month + 1
                if newMonth > 9:
                    dateList[0] = 1
                    dateList[1] = str(newMonth)[1]
                else:
                    dateList[0] = '0'
                    dateList[1] = str(newMonth)

            else:
                # change day
                remainder = (day + 4) - 28
                dateList[2] = '0'
                dateList[3] = str(remainder)
                # change month
                dateList[0] = '0'
                dateList[1] = '3'
        else:
            # adjust year
            year = int(self.date[4:])
            nextyear = year + 1
            for i in range(4):
                dateList[i + 4] = str(nextyear)[i]
            # adjust month
            dateList[0] = '0'
            dateList[1] = '1'
            # adjust day
            remainder = (day + 4) - 31
            dateList[2] = '0'
            dateList[3] = str(remainder)
        dateString = ''
        for i in range(8):
            dateString += dateList[i]
        return dateString

    def ready_for_unfollow(self):
        currentDate = strftime("%m%d%Y")
        currentYear = int(currentDate[4:])
        currentMonth = int(currentDate[2:4])
        currentDay = int(currentDate[:2])
        yearExpire = int(self.unfollowDate[4:])
        monthExpire = int(self.unfollowDate[2:4])
        dayExpire = int(self.unfollowDate[:2])
        if yearExpire>currentYear:
            return False
        else:
            if monthExpire>currentMonth:
                return False
            else:
                if dayExpire>currentDay:
                    return False
                else:
                    return True



        '''date is the in the form monthDayYear so august 4th 1999 would be '08041999' 
        so date sum is the sum of these  numbers'''
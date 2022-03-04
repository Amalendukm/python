import datetime

class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    
    def __add__(self, obj):
        return datetime.timedelta(hours = self.__hours, minutes= self.__minutes, seconds = self.__seconds) + datetime.timedelta(hours = obj.__hours, minutes= obj.__minutes, seconds = obj.__seconds)
        
obj1 = Time(1,3,24)
obj2 = Time(0,2,0)
print(obj1+obj2)

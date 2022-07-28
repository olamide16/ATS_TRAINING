class Time:
    def __init__(self) :
        self._hour = 0
        self._minute = 0
        self._second = 0
    
    
    def setTime(self, hour, minute,second):
        
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)
    
    
    def setHour(self,hour):
        if 0 <= hour < 24:
            self._hour = hour
        else:
            raise ValueError(f"hour ({hour}) must be 0-23")
            
    
    def setMinute(self,minute):
        if 0 <= minute < 60:
            self._minute = minute
        else:
            raise ValueError(f"minute ({minute}) must be 0-59")
            
        
        
    def setSecond(self,second):
        if 0 <= second < 60:
            self._second = second
        else:
            raise ValueError(f"second ({second}) must be 0-59") 
             
    
    
    def getHour(self):
        return self._hour
    
    
    def getMinutes(self):
        return self._minute 
    
    
    def getSecond(self):
        return self._second     
    
    
    def printMilitary(self):
        
        print (self._hour, self._minute, self._second)
    
    
    def printStandard(self):
        
        standardTime =""
        
        if self._hour == 0 or self._hour == 12:
            standardTime += "12:"
        else:
            standardTime += "%d:" % (self._hour %12)
        
        standardTime += "%.2d:%.2d" % (self._minute,self._second)
        
        if self._hour < 12:
            standardTime += "AM"
        else:
            standardTime += "PM"
        
        print (standardTime),
time1 = Time()
# time1.printMilitary()
# time1.printStandard()
# time1.setTime( 13, 27, 6 )
# time1.printMilitary()
# time1.printStandard()
# time1.setHour(4)
# time1.setMinute(3)
# time1.setSecond(34)
# time1.printMilitary()
# time1.printStandard()
time1.setMinute(6)
time1.setHour(23)
time1.setSecond(14)
# time1.printMilitary()
time1.printStandard()
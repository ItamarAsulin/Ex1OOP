import json
class elevator:
    #id,speed,minFloor,maxFloor,closeTime,openTime,startTime,stopTime
    def __init__(self,id,speed,minFloor,maxFloor,closeTime,openTime,startTime,stopTime):
        self.id=id
        self.speed=speed
        self.minFloor=minFloor
        self.maxFloor=maxFloor
        self.closeTime=closeTime
        self.openTime=openTime
        self.startTime=startTime
        self.stopTime=stopTime

    def __str__(self) -> str:
        return f"id:{self.id} ,speed:{self.speed} ,minF:{self.minFloor}" \
               f" ,maxF:{self.maxFloor} ,closeT:{self.closeTime} " \
               f",openT:{self.openTime} ,startT:{self.startTime} ,stopT:{self.stopTime}\n"

    def __repr__(self) -> str:
        return self.__str__()
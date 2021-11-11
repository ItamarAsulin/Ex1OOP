import json
from elevator import elevator
class Building:
    def __init__(self,minFloor,maxFloor,elevators):
        self.minFloor=minFloor
        self.maxFloor=maxFloor
        self.elevators=elevators

    def fromJson(self,building_j):
        with open(building_j,"r") as f:
            building_d = json.load(f)
            self.minFloor=building_d["_minFloor"]
            self.maxFloor=building_d["_maxFloor"]
            self.elevators=[]
            for e in building_d["_elevators"]:
                id = e["_id"]
                speed = e["_speed"]
                minFloor = e["_minFloor"]
                maxFloor = e["_maxFloor"]
                closeTime = e["_closeTime"]
                openTime = e["_openTime"]
                startTime = e["_startTime"]
                stopTime = e["_stopTime"]
                self.elevators.append(elevator(id,speed,minFloor,maxFloor,closeTime,openTime,startTime,stopTime))


    def __str__(self) -> str:
        return f"minFloor:{self.minFloor} ,maxFloor:{self.maxFloor} ,elevators:{self.elevators}\n"

    def __repr__(self) -> str:
        return self.__str__()


if __name__== '__main__':
    b1=Building(0,0,[])
    print(b1)
    b1.fromJson("B2.json")
    print(b1)
    b1.fromJson("B2.json")
    print(b1)




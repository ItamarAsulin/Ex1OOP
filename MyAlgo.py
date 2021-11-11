from csv import reader
from Building import Building
from elevator import elevator
from CallForElevator import CallForElevator
import math
class MyAlgo:
    def __init__(self, building, fileOfCalls, building_json):
        self.building=building.fromJson(building_json)
        open_file = open(fileOfCalls)
        read_file = reader(open_file)
        Calls_data = list(read_file)
        self.Calls_list=[]
        for c in Calls_data:
            time=c[1]
            src=c[2]
            dest=c[3]
            type=c[4]
            allocatedTo=c[5]
            self.Calls_list.append(CallForElevator(time,src,dest,type,allocatedTo))

    def how_many_elevators(self): #how many elevators there are in the building
        return len(self.building.elevators)

    def split_by_type(self): #split the list of calls to 2 list by type (up and down)
        listUp=[]
        listDown=[]
        for c in self.Calls_list:
            if c.src-c.dest>0:
                listDown.append(c)
                c.type=-1
            else:
                listUp.append(c)
                c.type=1
        return listUp,listDown


    def sort_by_time(self,listOfCalls): #sort the list of calls by time
        listOfCalls.sort(key=lambda c:c.time)
        return listOfCalls

    def long_calls(self,listOfCalls): #get a list of calls and return a list including all the long calls-
# long call is greater than a 1/3 building heigh
        longCalls=[]
        building_heigh= math.fabs(self.building.maxFloor-self.building.minFloor)
        for c in listOfCalls:
            if math.fabs(c.src-c.dest)>building_heigh/3:
                longCalls.append(c)
        return longCalls





    # def AllocateTo(self,c):


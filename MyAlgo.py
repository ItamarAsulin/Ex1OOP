from csv import reader
from Building import Building
from elevator import elevator
from CallForElevator import CallForElevator
import math
class MyAlgo:
    def __init__(self, building, fileOfCalls, building_json,output_csv):
        self.output_csv=output_csv
        self.building=building
        self.building.fromJson(building_json)
        open_file = open(fileOfCalls)
        read_file = reader(open_file)
        Calls_data = list(read_file)
        self.Calls_list=[]
        for c in Calls_data:
            time=float(c[1])
            src=int(c[2])
            dest=int(c[3])
            type=c[4]
            allocatedTo=int(c[5])
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


    def calls_sort_by_time(self,listOfCalls): #sort the list of calls by time
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

    def elevators_sort_by_speed(self): #build a list of the elevators and sort the list by speed
        elevators_list=[]
        for e in self.building.elevators:
            elevators_list.append(e)
        elevators_list.sort(key=lambda e:e.speed)
        return elevators_list

    def calls_sort_by_src(self,listOfCalls): #sort the list of calls by src level
        listOfCalls.sort(key=lambda c:c.src)
        return listOfCalls

    def calls_sort_by_dest(self,listOfCalls): #sort the list of calls by dest level
        listOfCalls.sort(key=lambda c:c.dest)
        return listOfCalls

    def __str__(self) -> str:
        return f"building:{self.building} ,Calls:{self.Calls_list}"

    def __repr__(self) -> str:
        return self.__str__()

    # def allocateTo(self):






# if __name__== '__main__':
#     b1=Building(0,0,[])
#     ohad=MyAlgo(b1,"Calls_a.csv","B4.json")
#     myCalls=[]
#     ohad.split_by_type()
#     # print(ohad.calls_sort_by_src(ohad.Calls_list))
#     for c in ohad.Calls_list:
#         if c.src==-1:
#             myCalls.append(c)
#     up=[]
#     down=[]
#     for c in myCalls:
#         if c.type==1:
#             up.append(c)
#         else:
#             down.append(c)
#     up=ohad.calls_sort_by_time(up)
#     print(up)
#     newUp=[]
#     for i in range (0, len(up)-1):
#         if up[i+1]-up[i].time<=15:






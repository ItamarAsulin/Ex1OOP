from csv import reader
from Building import Building
from elevator import elevator
from CallForElevator import CallForElevator
import math
from MyAlgo import MyAlgo
Building_json=input("enter your building json name/path here")
Calls_csv=input("enter your Calls csv name/path here")
output_csv=input("enter your output csv name/path here")
buildingToRun=Building(0,0,[])
AlgoToDo=MyAlgo(buildingToRun,Calls_csv,Building_json,output_csv)


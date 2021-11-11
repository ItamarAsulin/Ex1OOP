from csv import reader
from Building import Building
from Elevator import elevator
from CallForElevator import CallForElevator
import math
import sys
from MyAlgo import MyAlgo
# Building_json, Calls_csv, output_csv = input().split()
Building_json= sys.argv[1]
Calls_csv= sys.argv[2]
output_csv=sys.argv[3]
buildingToRun=Building(0,0,[])
AlgoToDo=MyAlgo(buildingToRun,Calls_csv,Building_json,output_csv)


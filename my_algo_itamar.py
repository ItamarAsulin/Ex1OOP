import json
import sys
from csv import *
from call_for_elevator import CallForElevator
from building import Building
from elevator import Elevator
import pandas as pd


class MyAlgoItamar:

    def __init__(self, building_json, calls_csv, output_csv):
        self.building = Building(0, 0, [])
        self.building.fromJson(building_json)
        self.calls_csv = calls_csv
        self.output_csv = output_csv
        self.calls_list = []
        self.initiate_calls_from_csv()
        self.elevators_dest = []
        self.elevators_finish_time = []
        self.num_of_elevators = len(self.building.elevators)
        for i in range(0, self.num_of_elevators):
            self.elevators_dest.append("0")
            self.elevators_finish_time.append("0")

    def initiate_calls_from_csv(self):
        open_file = open(self.calls_csv)
        read_file = reader(open_file)
        calls_data = list(read_file)

        for c in calls_data:
            time = float(c[1])
            src = int(c[2])
            dest = int(c[3])
            type = c[4]
            allocatedTo = int(c[5])
            self.calls_list.append(CallForElevator(time, src, dest, type, allocatedTo))

    def allocate_elev_to_call(self, src, dest, call_time):
        best_elev = 0
        min_time = float(sys.float_info.max)

        for i in range(0, self.num_of_elevators):
            curr_time = float(self.calculate_finish_time(i, src, dest, call_time))
            if curr_time < min_time:
                min_time = curr_time
                best_elev = i

        self.elevators_dest[best_elev] = dest
        self.elevators_finish_time = str(min_time)
        return best_elev

    def calculate_finish_time(self, index, src, dest, call_time):
        current_elevator = self.building.elevators[index]
        speed = float(current_elevator.speed)
        stop_time = float(current_elevator.stop_time)
        start_time = float(current_elevator.start_time)
        open_doors_time = float(current_elevator.open_time)
        close_doors_time = float(current_elevator.close_time)
        current_dest = int(self.elevators_dest[index])
        current_finish_time = self.elevators_finish_time[index]
        total_stop_time = float(2 * (stop_time + start_time + open_doors_time + close_doors_time))
        distance_from_current_floor_to_src = float(dist(current_dest, src))
        distance_from_src_to_dest = float(dist(src, dest))
        total_distance = float(distance_from_src_to_dest + distance_from_current_floor_to_src)
        total_travel_time = float(total_distance/speed)

        if float(current_finish_time) < float(call_time):
            expected_finish_time = float(call_time) + total_stop_time + total_travel_time
            return float(expected_finish_time)

        else:
            expected_finish_time = float(current_finish_time) + total_stop_time + total_travel_time
            return float(expected_finish_time)


def dist(floor_a, floor_b):
    a = int(floor_a)
    b = int(floor_b)
    ans = abs(a - b)
    return ans

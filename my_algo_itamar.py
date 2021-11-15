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
        self.elevators_src = []
        self.elevators_start_time = []
        self.num_of_elevators = len(self.building.elevators)
        for i in range(0, self.num_of_elevators):
            self.elevators_dest.append("0")
            self.elevators_finish_time.append("0")
            self.elevators_src.append("0")
            self.elevators_start_time.append("0")

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
        best_elev_index = 0
        min_time = float(sys.float_info.max)
        if self.num_of_elevators == 1:
            return 0

        for i in range(0, self.num_of_elevators):
            curr_time = self.calculate_finish_time(i, src, dest, call_time)
            if curr_time < min_time:
                min_time = curr_time
                best_elev_index = i
        best_elev = self.building.elevators[best_elev_index]
        elev_src = self.elevators_src[best_elev_index]
        elev_dest = self.elevators_dest[best_elev_index]
        call_dir = get_direction(src, dest)
        elev_dir = get_direction(elev_src, elev_dest)
        dist_from_elev_dest_to_call_src = float(dist(elev_dest, src))
        if call_dir == elev_dir:
            if elev_dir == "up":
                if self.is_a_possible_stop(best_elev_index, src, call_time):
                    if dest < elev_dest:
                        self.elevators_finish_time[best_elev_index] = min_time
                        return best_elev_index
                    else:
                        self.elevators_dest[best_elev_index] = dest
                        self.elevators_finish_time[best_elev_index] = min_time
                        return best_elev_index
                else:
                    elev_speed = float(best_elev.speed)
                    time_from_elev_dest_to_call_src = dist_from_elev_dest_to_call_src/elev_speed
                    arrival_time_to_call_src = float(self.elevators_finish_time[best_elev_index]) + time_from_elev_dest_to_call_src
                    self.elevators_start_time[best_elev_index] = arrival_time_to_call_src
                    self.elevators_src[best_elev_index] = src
                    self.elevators_finish_time[best_elev_index] = min_time
                    self.elevators_dest[best_elev_index] = dest
                    return best_elev_index

            else:
                if self.is_a_possible_stop(best_elev_index, src, call_time):
                    if dest > elev_dest:
                        self.elevators_finish_time[best_elev_index] = min_time
                        return best_elev_index
                    else:
                        self.elevators_dest[best_elev_index] = dest
                        self.elevators_finish_time[best_elev_index] = min_time
                        return best_elev_index
                else:
                    elev_speed = float(best_elev.speed)
                    time_from_elev_dest_to_call_src = dist_from_elev_dest_to_call_src / elev_speed
                    arrival_time_to_call_src = float(self.elevators_finish_time[best_elev_index]) + time_from_elev_dest_to_call_src
                    self.elevators_start_time[best_elev_index] = arrival_time_to_call_src
                    self.elevators_src[best_elev_index] = src
                    self.elevators_finish_time[best_elev_index] = min_time
                    self.elevators_dest[best_elev_index] = dest
                    return best_elev_index

        else:
            elev_speed = float(best_elev.speed)
            time_from_elev_dest_to_call_src = dist_from_elev_dest_to_call_src / elev_speed
            arrival_time_to_call_src = float(self.elevators_finish_time[best_elev_index]) + time_from_elev_dest_to_call_src
            self.elevators_start_time[best_elev_index] = arrival_time_to_call_src
            self.elevators_src[best_elev_index] = src
            self.elevators_finish_time[best_elev_index] = min_time
            self.elevators_dest[best_elev_index] = dest
            return best_elev_index

    def calculate_finish_time(self, index, src, dest, call_time):
        current_elevator = self.building.elevators[index]
        speed = float(current_elevator.speed)
        stop_time = float(current_elevator.stop_time)
        start_time = float(current_elevator.start_time)
        open_doors_time = float(current_elevator.open_time)
        close_doors_time = float(current_elevator.close_time)
        current_dest = int(self.elevators_dest[index])
        current_src = int(self.elevators_src[index])
        current_finish_time = float(self.elevators_finish_time[index])
        current_start_time = float(self.elevators_start_time[index])
        total_stop_time = float(2 * (stop_time + start_time + open_doors_time + close_doors_time))
        elev_dir = get_direction(current_src, current_dest)

        if float(current_finish_time) < float(call_time):
            total_distance = dist(current_dest, src) + dist(src, dest)
            total_travel_time = total_distance / speed
            expected_finish_time = float(call_time) + total_stop_time + total_travel_time
            return float(expected_finish_time)

        elif self.is_a_possible_stop(index, src, call_time):
            if elev_dir == "up":

                if int(dest) < current_dest:
                    expected_finish_time = current_finish_time + total_stop_time
                    return expected_finish_time
                else:
                    total_distance = dist(current_src, current_dest) + dist(current_dest, dest)
                    expected_finish_time = current_start_time + total_distance / speed + total_stop_time
                    return expected_finish_time

            else:

                if int(dest) > current_dest:
                    expected_finish_time = current_finish_time + total_stop_time
                    return expected_finish_time
                else:
                    total_distance = dist(current_src, current_dest) + dist(current_dest, dest)
                    expected_finish_time = current_start_time + total_distance / speed + total_stop_time
                    return expected_finish_time

        else:
            total_distance = dist(current_dest, src) + dist(src, dest)
            total_travel_time = total_distance / speed
            expected_finish_time = float(current_finish_time) + total_stop_time + total_travel_time
            return float(expected_finish_time)

    def get_current_positition(self, index, time):
        elev_src_floor = self.elevators_src[index]
        elev_speed = float(self.building.elevators[index].speed)
        elev_src_time = self.elevators_start_time[index]
        time_passed = float(time) - float(elev_src_time)
        elev_dir = get_direction(self.elevators_src[index], self.elevators_dest[index])
        if elev_dir == "up":
            current_position = int(elev_src_floor) + int(elev_speed * time_passed)
        else:
            current_position = int(elev_src_floor) - int(elev_speed * time_passed)
        return current_position

    def is_a_possible_stop(self, index, src, time):
        current_elev_position = self.get_current_positition(index, time)
        elev_dir = get_direction(self.elevators_src[index], self.elevators_dest[index])
        if elev_dir == "up":
            if current_elev_position < int(src):
                return True
            else:
                return False
        else:
            if current_elev_position > int(src):
                return True
            else:
                return False


def dist(floor_a, floor_b):
    a = int(floor_a)
    b = int(floor_b)
    ans = abs(a - b)
    return ans


def get_direction(floor_src, floor_dest):
    if floor_src < floor_dest:
        return "up"
    else:
        return "down"

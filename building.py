import json
from elevator import Elevator


class Building:

    def __init__(self, min_floor, max_floor, elevators):
        self.minFloor = min_floor
        self.maxFloor = max_floor
        self.elevators = elevators

    def fromJson(self, building_json):
        with open(building_json, "r") as f:
            building_d = json.load(f)
            self.minFloor = building_d["_minFloor"]
            self.maxFloor = building_d["_maxFloor"]
            # יא תחת
            self.elevators = []
            for e in building_d["_elevators"]:
                id = e["_id"]
                speed = e["_speed"]
                min_floor = e["_minFloor"]
                max_floor = e["_maxFloor"]
                close_time = e["_closeTime"]
                open_time = e["_openTime"]
                start_time = e["_startTime"]
                stop_time = e["_stopTime"]
                self.elevators.append(Elevator(id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time))

    def __str__(self) -> str:
        return f"minFloor:{self.minFloor} ,maxFloor:{self.maxFloor} ,elevators:{self.elevators}\n"

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == '__main__':
    b1 = Building(0, 0, [])
    print(b1)
    b1.fromJson("B2.json")
    print(b1)
    b1.fromJson("B2.json")
    print(b1)

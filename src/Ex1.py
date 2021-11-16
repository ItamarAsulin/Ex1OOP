import csv
from csv import reader
from building import Building
from elevator import Elevator
import math
from my_algo import *
import sys


building_json = sys.argv[1]
calls_csv = sys.argv[2]
output_csv = sys.argv[3]
algo_to_run = MyAlgo(building_json, calls_csv, output_csv)
calls = {}
i = 0

with open(calls_csv) as f:
    data = csv.reader(f)
    for row in data:
        calls[i] = row
        i += 1
    f.close()

j = 0
for j in range(0, i):
    row_to_add = calls.get(j)
    src = row_to_add[2]
    dest = row_to_add[3]
    time = row_to_add[1]
    index_of_allocated_elev = algo_to_run.allocate_elev_to_call(src, dest, time)
    row_to_add[5] = index_of_allocated_elev

j = 0
with open(output_csv, "w", newline='') as f:
    writer = csv.writer(f)
    for j in range(0,i):
        row_to_add = calls.get(j)
        writer.writerow(row_to_add)
    f.close()

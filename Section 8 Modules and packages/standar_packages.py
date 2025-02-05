import array

arr = array.array("i", [1, 2, 3, 4])
print(arr)

import math

print(math.sqrt(16))
print(math.pi)

import random

print(random.randint(1, 10))

print(random.choice(["Apple", "Banna", "Cherry", 4, 5]))

# File and directory access
import os

print(os.getcwd())
os.mkdir("Section 8 Modules and packages/test_dir")

import shutil

source_file_path = "Section 8 Modules and packages/source.txt"
destination_file_path = "Section 8 Modules and packages/test_dir/destination.txt"
shutil.copy(source_file_path, destination_file_path)

# Data Serialization
import json

data = {"name": "John", "age": 30, "city": "New York"}
json_data = json.dumps(data)
print(json_data)
print(type(json_data))
original_data = json.loads(json_data)
print(original_data)
print(type(original_data))

# CSV
import csv

with open("Section 8 Modules and packages/data.csv", "w", newline="") as file:
    write = csv.writer(file)
    write.writerow(["Name", "Age"])
    write.writerow(["John", 30])
    write.writerow(["Jenny", 25])
    write.writerow(["Jack", 40])

with open("Section 8 Modules and packages/data.csv", "r") as file:
    read = csv.reader(file)
    for row in read:
        print(row)


from datetime import datetime, timedelta

now = datetime.now()
print(now)

yesterday = now - timedelta(days=1)
print(yesterday)

import time

print(time.time())
time.sleep(2)
print(time.time())

import re

pattern = r"\d+"
text = "The are 123 apples"
match = re.search(pattern, text)
print(match.group())

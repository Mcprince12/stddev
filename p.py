import csv
import math

with open("csv files/data.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]


def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total = total+int(x)
    mean = total/n
    return mean


# Squaring and getting the values
squared_list = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squared_list.append(a)

# Getting the sum
sum = 0
for i in squared_list:
    sum = sum+i

# Dividing the sum by the total values-1
result = sum/(len(data)-1)

# Getting the deviation by taking the square root of the result
std_dev = math.sqrt(result)
print(std_dev)

from collections import deque

pumps_num = int(input())
pumps = deque()

for _ in range(pumps_num):
    current_fuel, distance = map(int, input().split())
    pumps.append({"fuel": current_fuel, "distance": distance})

start_position = 0
stops = 0

while stops < pumps_num:
    fuel = 0
    for i in range(pumps_num):
        fuel += pumps[i]["fuel"]
        distance = pumps[i]["distance"]
        if fuel < distance:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start_position)
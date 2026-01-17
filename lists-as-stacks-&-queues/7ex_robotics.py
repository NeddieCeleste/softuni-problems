from collections import deque


def time_changes(begin_time, elapsed_time):
    total_seconds = begin_time[0] * 3600 + begin_time[1] * 60 + begin_time[2] + elapsed_time

    h = (total_seconds // 3600) % 24
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return [h, m, s]


robot_input = input().split(";")
starting_time = list(map(int, input().split(":")))
command_queue = deque()

robot_processing = []
for robot_log in robot_input:
    name, time = robot_log.split("-")
    robot_processing.append({"Name": name, "Time": int(time), "NextFree": 0})

while True:
    command = input()
    if command == "End":
        break
    command_queue.append(command)

timer = 0
while command_queue:
    timer += 1
    current_product = command_queue.popleft()
    assigned_product = False

    for robot in robot_processing:
        if robot["NextFree"] <= timer:
            robot["NextFree"] = timer + robot["Time"]

            h, m, s = time_changes(starting_time, timer)
            print(f"{robot['Name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")

            assigned_product = True
            break

    if not assigned_product:
        command_queue.append(current_product)
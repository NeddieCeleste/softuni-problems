from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

all_cars = deque()
cars_passed = 0
crash = False

while True:
    command = input()

    if command == "END":
        break

    if command == "green":
        current_green = green_light_duration

        while all_cars and current_green > 0:
            car = all_cars.popleft()

            if len(car) <= current_green:
                current_green -= len(car)
                cars_passed += 1
            else:
                total_time_allowed = current_green + free_window_duration

                if len(car) <= total_time_allowed:
                    cars_passed += 1
                    current_green = 0
                else:
                    hit_index = total_time_allowed
                    print("A crash happened!")
                    print(f"{car} was hit at {car[hit_index]}.")
                    crash = True
                    break

        if crash:
            break

    else:
        all_cars.append(command)

if not crash:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
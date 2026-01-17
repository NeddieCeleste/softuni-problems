from collections import deque

all_cups = (int(x) for x in input().split())
all_bottles = (int(x) for x in input().split())
total_cups_queue = deque(all_cups)
total_bottles_stack = list(all_bottles)
wasted_water = 0


while total_cups_queue:
    current_cup = total_cups_queue.popleft()
    while current_cup > 0 and total_bottles_stack:
        current_bottle = total_bottles_stack.pop()
        if current_cup <= current_bottle:
            wasted_water += current_bottle - current_cup
            current_cup -= current_bottle
        elif current_cup > current_bottle:
            current_cup -= current_bottle
    if not total_bottles_stack:
        break

if not total_cups_queue:
    print(f"Bottles: {' '.join(str(x) for x in total_bottles_stack)}")
else:
    print(f"Cups: {' '.join(str(x) for x in total_cups_queue)}")

print(f"Wasted liters of water: {wasted_water}")












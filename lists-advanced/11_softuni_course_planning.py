def add_lesson(schedule, lesson):
    if lesson not in schedule:
        schedule.append(lesson)


def insert_lesson(schedule, lesson, index):
    if lesson not in schedule:
        if 0 <= index < len(schedule):
            schedule.insert(index, lesson)
        else:
            schedule.append(lesson)


def remove_lesson(schedule, lesson):
    if lesson in schedule:
        schedule.remove(lesson)
    exercise = f"{lesson}-Exercise"
    if exercise in schedule:
        schedule.remove(exercise)


def swap_lessons(schedule, lesson1, lesson2):
    if lesson1 in schedule and lesson2 in schedule:
        i1, i2 = schedule.index(lesson1), schedule.index(lesson2)
        schedule[i1], schedule[i2] = schedule[i2], schedule[i1]

        # handle exercise for lesson1
        ex1 = f"{lesson1}-Exercise"
        if ex1 in schedule:
            schedule.remove(ex1)
            schedule.insert(schedule.index(lesson1) + 1, ex1)

        # handle exercise for lesson2
        ex2 = f"{lesson2}-Exercise"
        if ex2 in schedule:
            schedule.remove(ex2)
            schedule.insert(schedule.index(lesson2) + 1, ex2)


def add_exercise(schedule, lesson):
    exercise = f"{lesson}-Exercise"

    if lesson in schedule:
        if exercise not in schedule:
            index = schedule.index(lesson)
            schedule.insert(index + 1, exercise)
    else:
        schedule.append(lesson)
        schedule.append(exercise)


# ---------------- MAIN PROGRAM ---------------- #

schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    parts = command.split(":")
    action = parts[0]

    if action == "Add":
        add_lesson(schedule, parts[1])

    elif action == "Insert":
        insert_lesson(schedule, parts[1], int(parts[2]))

    elif action == "Remove":
        remove_lesson(schedule, parts[1])

    elif action == "Swap":
        swap_lessons(schedule, parts[1], parts[2])

    elif action == "Exercise":
        add_exercise(schedule, parts[1])


# print result
for i, lesson in enumerate(schedule, start=1):
    print(f"{i}.{lesson}")
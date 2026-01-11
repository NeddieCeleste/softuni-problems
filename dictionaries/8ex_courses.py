course_dictionary = {}
count = 0
while True:
    command = input()
    if command == "end":
        break

    course, name = command.split(" : ")
    if course not in course_dictionary:
        course_dictionary[course] = [name]
    else:
        course_dictionary[course].append(name)

for course in course_dictionary.keys():
    print(f"{course}: {len(course_dictionary[course])}")
    for name in course_dictionary[course]:
        print(f"-- {name}")




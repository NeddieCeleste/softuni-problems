from math import ceil

number_people = int(input())
elevator_capacity = int(input())
courses = ceil(number_people / elevator_capacity)
print(courses)
students_dictionary = {}
number_pairs = int(input())
for _ in range(number_pairs):
    student_name = input()
    grade = float(input())
    if student_name not in students_dictionary.keys():
        students_dictionary[student_name] = [grade]
    else:
        students_dictionary[student_name].append(grade)
for student in students_dictionary.keys():
    average = sum(students_dictionary[student]) / len(students_dictionary[student])
    if average >= 4.50:
        print(f"{student} -> {average:.2f}")

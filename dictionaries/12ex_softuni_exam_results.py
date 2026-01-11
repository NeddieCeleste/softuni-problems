user_points_dictionary = {}
submission_dictionary = {}
while True:
    current_result = input().split("-")
    if len(current_result) == 1:
        break
    elif len(current_result) == 2:
        user = current_result[0]
        del user_points_dictionary[user]
    else:
        name, course, points = current_result[0], current_result[1], int(current_result[2])
        if name not in user_points_dictionary.keys():
            user_points_dictionary[name] = 0
        if points > user_points_dictionary[name]:
            user_points_dictionary[name] = points
        if course not in submission_dictionary.keys():
            submission_dictionary[course] = 0
        submission_dictionary[course] += 1
print("Results:")
for username, point in user_points_dictionary.items():
    print(f"{username} | {point}")
print("Submissions:")
for language, submissions_count in submission_dictionary.items():
    print(f"{language} - {submissions_count}")
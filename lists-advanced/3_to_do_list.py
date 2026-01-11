final_list = [0] * 10

while True:
    command = input()
    if command != 'End':
        importance_note = command.split("-")
        index = int(importance_note[0]) - 1
        note = importance_note[1]
        final_list.pop(index)
        final_list.insert(index, note)
        result = [element for element in final_list if element != 0]


    else:
        print(result)
        break



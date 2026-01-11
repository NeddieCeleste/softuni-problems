string_name = input()
output = ""
while string_name != "End":
    if string_name != "SoftUni":
        for character in string_name:
            output = output + character*2
        print(output)

        output = ""
        string_name = input()
    else:
        string_name = input()
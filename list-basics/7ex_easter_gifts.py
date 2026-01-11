gifts_list = input().split()
word = ""
command = input()
while command != "No Money":
    separate_text = command.split()
    if separate_text[0] == "OutOfStock":
        if len(separate_text) > 1:
            word = separate_text[1]
            gifts_list = ["None" if x == word else x for x in gifts_list]
    elif separate_text[0] == "Required":
        if len(separate_text) > 2:
            word = separate_text[1]
            index_cmd = int(separate_text[2])
            if 0 <= index_cmd < len(gifts_list):
                gifts_list[index_cmd] = word
    elif separate_text[0] == "JustInCase":
        if len(separate_text) > 1:
            word = separate_text[1]
            gifts_list[-1] = word
    command = input()

final_gifts = [gift for gift in gifts_list if gift != "None"]
print(" ".join(final_gifts))
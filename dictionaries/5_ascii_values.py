characters = input().split(', ')
students = {character: ord(character) for character in characters}
print(students)
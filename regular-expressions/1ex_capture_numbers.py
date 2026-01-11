import re

all_matches = []
line = input()
pattern = r"\d+"
while line:
    matches = re.findall(pattern, line)
    if matches:
        all_matches += matches
    line = input()
print(" ".join(all_matches))

import re

line = "Piękny jest lepszy niż brzydki,"

matches = re.findall("Piękny", line)

print(matches)

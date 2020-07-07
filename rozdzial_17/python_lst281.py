
import re

line = "Piękny jest lepszy niż brzydki,"

matches = re.findall("piękny", line, re.IGNORECASE)

print(matches)

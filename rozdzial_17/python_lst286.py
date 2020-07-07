import re

line = "Kocham $"

m = re.findall("\\$",
               line,
               re.IGNORECASE)

print(m)

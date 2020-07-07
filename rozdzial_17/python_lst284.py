
import re

t = "__jeden__ __dwa__ __trzy__"

results = re.findall("__.*?__", t)

for match in results:
    print(match)

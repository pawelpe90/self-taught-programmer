
import re

string = "Dwa drwa."

m = re.findall("[dr]wa",
          string,
          re.IGNORECASE)
print(m)

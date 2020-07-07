
import csv

# upewnij się, że istnieje 
# plik utworzony,
# w poprzednim przykładzie

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

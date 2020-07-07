
qs = ["Jak masz na imię?",
      "Jaki jest twój ulubiony kolor?",
      "Jakie masz zadanie?"]
n = 0
while True:
    print("Wpisz q, aby zakończyć")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3


# Uwaga: wartość w konsoli należy wpisać jako łańcuch
# znaków (np.: '3'), a nie jako liczbę (3)!

rhymes = {"1": "niebem",
          "2": "kwa kwa",
          "3": "śni",
          "4": "ordery",
          "5": "cięć"
          }


n = input("Wpisz cyfrę: ")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Nie znaleziono.")

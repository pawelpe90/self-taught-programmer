numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Odgadnij liczbę lub wpisz q, aby wyjść.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("wpisz liczbę lub naciśnij klawisz q, aby wyjść.")
    if answer in numbers:
        print("Udało ci się odgadnąć!")
    else:
        print("Nie udało ci się odgadnąć!")

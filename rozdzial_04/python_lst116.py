
try:
    a = input("wpisz liczbę: ")
    b = input("wpisz drugą liczbę: ")
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("Nieprawidłowe dane wejściowe.")


a = input("wpisz liczbę: ")
b = input("wpisz drugą liczbę: ")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("drugą liczbą nie może być 0.")

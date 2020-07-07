def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Nie można skonwertować łańcucha na liczę zmiennoprzecinkową.")

c = convert("55.0")
print(c)

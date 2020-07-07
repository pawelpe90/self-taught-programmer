answer = input("Jaki jest twój ulubiony kolor?")
with open("fav_color.txt", "w") as f:
    f.write(answer)

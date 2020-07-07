
colors = ["niebieski","zielony","czerwony"]

guess = input("Zgadnij jaki kolor wybrałem? ")

print( guess )

if guess in colors:
    print("Zgadłeś!")
else:
    print("Źle. Spróbuj jeszcze raz.")


rock = []
country = []


def collect_songs():
    song = "Wisz tytuł piosenki."
    ask = "Naciśnij r lub c, albo q by wyjść."

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)

        elif genre ==("c"):
            cy = input(song)
            country.append(cy)

        else:
            print("Nieprawidłowe polecenie.")
    print(rock)
    print(country)

collect_songs()

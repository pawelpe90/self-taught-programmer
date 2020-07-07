me = {
    "height": "6",
    "fav_color": "red",
    "fav_author": "Orwell"
}

answer = input("Podaj wartości dla kluczy: height, fav_color oraz fav_author")
if answer in me:
    result = me[answer]
    print(result)

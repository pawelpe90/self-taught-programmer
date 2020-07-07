import csv

movies = [["Top Gun", "Ocean's Eleven", "Report mniejszości"], ["Titanic", "Ostatni Jedi", "Incepcja"],["Pulp Fiction", "Człowiek w ogniu", "Seksmisja"]]
with open("filmy.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)

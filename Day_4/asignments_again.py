## -1
from os import remove

movies = [(("Manhoi"), ("Manh"), ("2009"), ("528"))]

## -2
movie_title = input("Enter movie name: ")
director = input("Enter director: ")
release_year = input("Enter release year: ")
budget = input("Enter budget: ")

## -3
movie_new = movie_title, director, release_year, budget
print(movie_new)

## -4
print(f"{movie_new[0]}" "\n" f"{movie_new[2]}")

## -5
movies.append(movie_new)
print(movies)

## -6
print(movies[0])
print(movies[1])

## -7
del movies[0]
#movies.remove(movies[0])
print(movies)

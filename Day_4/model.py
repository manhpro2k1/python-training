movies = [
    ("The Room", "Tommy Wiseau", "2003", "$6,000,000")
]

title = input("Title: ")
director = input("Director: ")
year = input("Year of release: ")
budget = input("Budget: ")

new_movie = title, director, year, budget

print(f"{new_movie[0]} ({new_movie[2]})")

movies.append(new_movie)

print(movies[0])
print(movies[1])

del movies[0]
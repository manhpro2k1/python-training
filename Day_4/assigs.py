movies = [("maytrang", "nguyen", "2009", "12356")]

title = input("title: ")
director = input("director: ")
year = input("release_year: ")
money = input("budget: ")

new_movies = title, director, year, money

print(f'{new_movies[0]}')
print(f"{new_movies[2]}")

movies.append(new_movies)

print(movies[0])
print(movies[1])

del movies[0]
print(movies)

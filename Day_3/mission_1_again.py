## 1
greeting = "Hello, world"

print(f"{greeting}!")
greeting = "Hello, world{}"
print(greeting.format("!"))
greeting = "Hello, world"
print(greeting + str("!"))

## 2
name = input("Enter name user: ").title().strip()
print(f"Hello, {name}")

## 3
abc = " I am"
d = 29
print(f"{abc} {d}")
print("I am " + str("29"))

## 4
title = "Joker"
director = "Todd Phillips"
release_year = 2019
print(f"{title} {release_year}, directed by {director}")
# Joker (2019), directed by Todd Phillips

## project

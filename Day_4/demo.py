names = ["John", "Alice", "Sarah", "George"]
names.append("simon")
names = names +["manh"]
print(names[-1])
print(names[-2])
print(names[-4])  # George
movie_titles = [
    "Eternal Sunshine of the Spotless Mind",
    "Memento",
    "Requiem for a Dream"]
friend_details = ["John", 27, "Web Developer"]
print(friend_details)
numbers = [343.4,545.98,4,954.03,3.5]
print(numbers)

numbers = [1, 2, 4, 5]
numbers.insert(2, 3)
numbers.insert(7,3)

print(numbers)  # [1, 2, 3, 4, 5]

numbers = ["a, b, c, d, e, g, h"]
numbers.insert(5,"f")
print(numbers)

abc = ["John", "Sarah", "Alice", "Sarah", "George"]
abc.remove("Sarah")
print(abc)

d = ["a", "b", "c", "d"]
#del d[2]
#print(d)
d.pop()
print(d)
d.pop(1)
print(d)
last_in_line = d.pop()
print(last_in_line)
d.clear()
print(d)

name = "manh", "an", "hung", "huy"
name = "manh", "an", "hung", "huy"


movies = [("abc", 2009),
          ("manh", 2008),
          ("an", 2017)
          ]
name = ("John",)

movies = [
    ("Eternal Sunshine of the Spotless Mind", 2004),
    ("Memento", 2000),
    ("Requiem for a Dream", 2000)
]
movies[0]
print(movies)
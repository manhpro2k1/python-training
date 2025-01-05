movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for movie in movies:
    # Check the title of the current movie is Memento
    if movie[0] == "Memento":
        # If the title is Memento, inform the user that the movie exists and break the loop
        print("Memento is in the movie library!")
        break

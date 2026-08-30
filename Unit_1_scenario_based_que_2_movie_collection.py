class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    def category(self):
        if self.rating >= 8:
            return "Hit"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Flop"

    def display(self):
        print("Movie Name:", self.movie_name)
        print("Rating:", self.rating)
        print("Ticket Price:", self.ticket_price)
        print("Category:", self.category())

class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\n--- Movie Details ---")
        for movie in self.movies:
            movie.display()

cinema = Cinema()

n = int(input("Enter number of movies: "))

for i in range(n):
    print(f"\nEnter details of Movie {i+1}")
    name = input("Movie Name: ")
    rating = float(input("Rating: "))
    price = float(input("Ticket Price: "))

    movie = Movie(name, rating, price)
    cinema.add_movie(movie)

cinema.display_movies()

from app.cinema.customer import Customer
from app.cinema.cinema_stuff import Cleaner


class CinemaHall:

    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name: str, customer: list, cleaning_stuff):
        print(f"\"{movie_name}\" started in hall number {self.number}.")
        for c in customer:
            c.watch_movie(movie_name)
        print(f"\"{movie_name}\" ended.")
        cleaner = Cleaner(cleaning_stuff)
        cleaner.clean_hall(self.number)

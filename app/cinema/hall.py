from ..people.customer import Customer
from ..people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name: str, customers: list[Customer], cleaning_staff: Cleaner):
        print(f"Movie session in Hall {self.number} starts. Movie: {movie_name}")

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f"Movie session in Hall {self.number} ends. Movie: {movie_name}")

        cleaning_staff.clean_hall(self.number)

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, num_hall: int) -> None:
        self.num_hall = num_hall

    def movie_session(self, movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:
        print(f"The movie {movie_name} is starting in hall {self.num_hall}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"The movie {movie_name} has ended in hall {self.num_hall}.")
        cleaning_staff.clean_hall(self.num_hall)

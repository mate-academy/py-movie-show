from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    """This class describes actions during the movie session"""

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list[Customer], cleaning_staff: list[Cleaner]) -> str:
        print(f"{movie_name} started in hall number {self.number}")

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f"'{movie_name}' ended")

        cleaning_staff.clean_hall(self.number)

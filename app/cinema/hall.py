from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self, movie_name: str,
            customers: list,
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)


if __name__ == "__main__":
    customers = [
        Customer(**{"name": "Bob", "food": "Coca-cola"}),
        Customer(**{"name": "Alex", "food": "popcorn"})
    ]
    hall_number = 5
    cleaner = Cleaner("Anna")
    movie = "Madagascar"

    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=cleaner
    )

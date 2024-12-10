from typing import List
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, mov: str, cust: List[Customer],
                      clean: Cleaner) -> None:

        print(f"\"{mov}\" started in hall number {self.number}.")

        for customer in cust:
            customer.watch_movie(mov)

        print(f"\"{mov}\" ended.")

        clean.clean_hall(self.number)

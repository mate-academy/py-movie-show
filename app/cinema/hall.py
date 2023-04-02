from typing import Any

from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: Any,
                      cleaning_staff: Cleaner | str) -> None:

        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')

        if not isinstance(cleaning_staff, Cleaner):
            clean = Cleaner(cleaning_staff)
            clean.clean_hall(self.number)
        else:
            clean = Cleaner(cleaning_staff.name)
            clean.clean_hall(self.number)

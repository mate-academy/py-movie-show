from __future__ import annotations
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for client in customers:
            client.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)

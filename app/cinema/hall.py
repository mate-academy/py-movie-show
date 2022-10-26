from __future__ import annotations
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie: str, custom: list, staff: Cleaner) -> None:
        print(f'"{movie}" started in hall number {self.number}.')
        for i in custom:
            i.watch_movie(movie)
        print(f'"{movie}" ended.')
        staff.clean_hall(self.number)

from __future__ import annotations
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number
    # number of the hall in cinema

    def movie_session(self, movie: str, customers: list,
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie}" started in hall number {self.number}.')
        for cs in customers:
            cs.watch_movie(movie)
        print(f'"{movie}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)

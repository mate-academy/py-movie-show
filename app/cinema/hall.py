from __future__ import annotations
import app.people.customer as people_c
import app.people.cinema_staff as cs


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[people_c.Customer],
            cleaning_staff: cs.Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for i in customers:
            print(f'{i.name} is watching "{movie_name}".')
        print(f'"{movie_name}" ended.')
        cs.Cleaner.clean_hall(cleaning_staff, self.number)

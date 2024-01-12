from __future__ import annotations


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list[Customers], cleaning_stuff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie()
        print(f'"{movie_name}" ended')
        cleaning_stuff.clean_hall(number=self.number)


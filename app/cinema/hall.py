from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self._number = number

    def movie_session(
            self, movie_name: str,
            customers: list[Customer],
            cleaner: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self._number}.')
        for cust in customers:
            print(f'{cust.name} is watching "{movie_name}".')
        print(f'"{movie_name}" ended.')
        cleaner.clean_hall(self._number)

    @property
    def number(self) -> int:
        return self._number

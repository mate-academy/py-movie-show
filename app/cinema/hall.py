from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List


class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.number = hall_number

    def movie_session(
            self,
            movie_name: str,
            customers: List[Customer],
            cleaning_staff: Cleaner
    ) -> None:

        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}\" ended.')
        cleaning_staff.clean_hall(self.number)

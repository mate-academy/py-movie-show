from typing import List
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: List[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        """
        Метод для проведення сеансу в кінозалі.

        Параметри:
        - movie_name: str, назва фільму.
        - customers:
        List[Customer], список екземплярів класу Customer,
        клієнти, які дивляться фільм.
        - cleaning_staff: Cleaner, екземпляр класу Cleaner, прибиральник.

        Повертає:
        None
        """
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list[Customer],
                      cleaner: Cleaner) -> str:
        result = []
        result.append(f'"{movie_name}" started in hall number '
                      f'{self.number}.\n')

        for customer in customers:
            result.append(f'{customer.name} is watching '
                          f'"{movie_name}".\n')

        result.append(f'"{movie_name}" ended.\n')
        result.append(f"Cleaner {cleaner.name} is cleaning hall number "
                      f"{self.number}.")

        return ''.join(result)
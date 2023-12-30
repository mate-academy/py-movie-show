from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    number = 0

    def __init__(self, number: int) -> None:
        self.number = number
        CinemaHall.number = self.number

    @classmethod
    def movie_session(cls, movie_name: str,
                      customers: list = Customer.customers,
                      cleaning_staff: str | object = Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {cls.number}.')
        for person in customers:
            Customer.watch_movie(person, movie_name)

        print(f'"{movie_name}" ended.')
        cleaning_staff = Cleaner(cleaning_staff).name
        cleaning_staff.clean_hall(cls.number)

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner
                      ) -> None:
        print(f'\"{movie_name}\" started in hall number {self.number}.')
        if type(customers[0]) is dict:
            for customer in customers:
                one_customer = Customer(customer.get("name"), customer.get("food"))
                one_customer.watch_movie(movie_name)
        else:
            for customer in customers:
                customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')

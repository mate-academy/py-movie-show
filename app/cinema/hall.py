from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: str
    ) -> None:
        print(f'\"{movie_name}\" started in hall number {self.number}.')
        for customer in customers:
            if type(customer) == Customer:
                customer_movie_session = customer
            else:
                customer_movie_session = Customer(
                    name=customer["name"],
                    food=customer["food"]
                )
            customer_movie_session.watch_movie(movie=movie_name)
        print(f'\"{movie_name}\" ended.')
        cleaning = Cleaner(cleaning_staff)
        cleaning.clean_hall(self.number)

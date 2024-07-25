from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: "Cleaner"
    ) -> str:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for person in customers:
            if isinstance(person, dict):
                customer = Customer(person["name"], person["food"])
            elif isinstance(person, Customer):
                customer = person
            else:
                raise TypeError("Each customer must be a dict or "
                                "Customer instance.")
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)

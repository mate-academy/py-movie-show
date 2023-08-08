from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
        self,
        movie_name: str,
        customers: list["Customer"],
        cleaning_staff: Cleaner,
    ) -> None:
        """ " TODO:
        that takes movie_name, customers - list of a customers
        (Customer instances), cleaning_staff -
        cleaner (Cleaner instance).
        This method prints about movie start, calls
        customers method watch_movie, prints about
        movie end, calls cleaner method clean_hall."""
        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        cleaning_staff.clean_hall(self.number)

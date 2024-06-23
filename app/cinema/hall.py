from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)


if __name__ == "__main__":
    ch = CinemaHall(5)
    customers = [
        Customer("Bob", "Coca-Cola"),
        Customer("Alex", "popcorn")
    ]
    cleaner = Cleaner("Anna")
    ch.movie_session(movie_name="Madagascar",
                     customers=customers,
                     cleaning_staff=cleaner)

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            customers: list[dict],
            cleaner: str,
            movie_name: str) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            Customer(
                customer["name"],
                customer["food"]
            ).watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        Cleaner(cleaner).clean_hall(self.number)

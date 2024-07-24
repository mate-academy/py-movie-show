from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> str:
        print(f"Movie: {movie_name} stars in hall number {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie: {movie_name} ends in hall number {self.number}.")
        cleaning_staff.clean_hall(self.number)

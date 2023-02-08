from app.people.clean_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:

    def __init__(self, name: str) -> None:
        self.name = name

    def movie_session(self,
                      movie_name: str,
                      customers: Customer,
                      cleaning_staff: Cleaner) -> str:
        print(f"{movie_name} starts at hall number {self.name}")
        for customer in customers:
            print(customer.watch_movie(movie_name))
        print(f"{movie_name} ended")
        print(cleaning_staff.clean_hall(self.name))

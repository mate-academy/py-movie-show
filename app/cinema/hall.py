from typing import List


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: List["Customer"], cleaning_staff: "Cleaner"):
        print(f"\"{movie_name}\" started in hall {self.number}")

        for customer in customers:
            customer.watch_movie()

        print(f"\"{movie_name}\" ended")

        cleaning_staff.clean_hall(self.number)

from typing import List


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: List["Customer"], cleaning_staff: "Cleaner"):


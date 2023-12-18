from app.cinema import bar
from app.people import customer


class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}")


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff: Cleaner) -> None:

        print(f'"{movie_name}" started in hall number {self.number}.')

        for cust in customers:
            cust1 = Custumer(cust)
            cust1.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        cleaning_staff.clean_hall(self.number)


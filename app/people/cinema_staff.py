from cinema.hall import CinemaHall

class Cleaner:

    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {CinemaHall.hall_number}")
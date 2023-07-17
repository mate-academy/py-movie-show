class Cleaner:
    def __init__(self, name: str):
        self.name = name

    def clean_hall(self):
        print(f"{self.name} is cleaning {CinemaHall.number}")

class Cleaner:
    cleaners = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.cleaners.append(self)

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")

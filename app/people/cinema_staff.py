from typing import NoReturn


class Cleaner:
    def __init__(self, name: str) -> NoReturn:
        self.name = name

    def clean_hall(self, hall_number: int) -> NoReturn:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")

# print(type(Cleaner.clean_hall))

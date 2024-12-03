from typing import Any


class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")

    def __str__(self) -> Any:
        return self.name


if __name__ == "__main__":
    anna = Cleaner(name="Anna")
    anna.clean_hall(hall_number=5)
    # Cleaner Anna is cleaning hall number 5.

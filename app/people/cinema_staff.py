class Cleaner:
    def __init__(self, name: str) -> None:
        self._name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self._name} is cleaning hall number {hall_number}.")

    @property
    def name(self) -> str:
        return self._name

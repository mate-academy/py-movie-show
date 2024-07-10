class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def clean_hall(hall_number: int) -> None:
        print(f"Cleaner {"self.name"} is cleaning hall {hall_number}")

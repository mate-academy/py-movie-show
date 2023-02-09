class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    #    print(f"Cleaner name = {self.name}")

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")

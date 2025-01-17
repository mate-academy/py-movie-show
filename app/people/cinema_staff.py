class Cleaner:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def clean_hall(self, hall_number: int ):
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")

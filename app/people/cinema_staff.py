class Cleaner:
    def __int__(self, name: str):
        self.name = name

    def clean_hall(self, hall_number: int):
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}")
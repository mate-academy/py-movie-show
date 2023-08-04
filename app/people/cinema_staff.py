class Cleaner:
    def __init__(self, name) -> None:
        self.name = name

    def clean_hall(self, hall_number) -> None:
        print(f"Cleaner {self.name} is cleaning "
              f"hall number {hall_number}.")

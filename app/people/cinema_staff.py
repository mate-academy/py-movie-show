from __future__ import print_function

class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"{self.name} is cleaning Hall {hall_number}")

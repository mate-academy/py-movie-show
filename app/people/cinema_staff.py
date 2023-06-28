class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean_hall(self, hall_number):
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")


if __name__ ==  "__main__":
    anna = Cleaner(name="Anna")
    anna.clean_hall(hall_number=7)



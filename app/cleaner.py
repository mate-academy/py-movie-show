class Cleaner:
    def __init__(self, name):
        self.name = name

    # Замените старый метод clean на clean_hall
    def clean_hall(self, hall_number):
        return f"Cleaner {self.name} is cleaning hall number {hall_number}."
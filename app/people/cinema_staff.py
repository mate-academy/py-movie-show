class Cleaner:
    def __init__(self, name: str) -> None:
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        """
        Метод для прибирання залу кінотеатру.

        Параметри:
        - hall_number: int, номер залу, який потрібно прибрати.

        Повертає:
        None
        """
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")

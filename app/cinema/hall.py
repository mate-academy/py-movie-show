class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: str
    ) -> None:

        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            print(f'{customer} is watching "{movie_name}".')

        print(f'"{movie_name}" ended.')
        print(f"Cleaner {cleaning_staff} is cleaning hall number "
              f"{self.number}.")

class CinemaHall:
    def __init__(self, number: int):
        self.movie_name = None
        self.customers = None
        self.cleaning_staff = None
        self.number = number

    def movie_session(
            self, movie_name: str,
            customers: list["Customer"],
            cleaning_staff: "Cleaner") -> None:
        print(f"{self.movie_name} started in {self.number} ")

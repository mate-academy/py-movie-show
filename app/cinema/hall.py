class CinemaHall:
    def __init__(self, number: int):
        self.number = number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff: list):
        print(f"{movie_name} started in hall number {self.number}.")
        # This method prints about movie start

        for customer in customers:
            customer.watch_movie(movie_name)
        # calls customers method watch_movie

        print(f"{movie_name} ended.")
        # prints about movie end

        Cleaner.clean_hall(self.number)
        # calls cleaner method clean_hall

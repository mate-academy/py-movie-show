class CinemaHall:
    def __init__(self, number_of_hall: int) -> None:
        self.number = number_of_hall

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_stuff: object
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended')
        cleaning_stuff.clean_hall(self.number)




# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.
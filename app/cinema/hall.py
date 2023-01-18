class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: any,
                      cleaning_staff: any
                      ) -> None:
        print(f""""{movie_name}" started in hall number {self.number}.""")
        for customer in customers:
            object_customer = customer
            object_customer.watch_movie(movie_name)
        print(f""""{movie_name}" ended.""")
        cleaning_staff.clean_hall(self.number)

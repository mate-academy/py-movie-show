from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)


# if __name__ == "__main__":
#     customers = [
#         {"name": "Bob", "food": "Coca-cola"},
#         {"name": "Alex", "food": "popcorn"}
#     ]
#     number = 5
#     cleaning_staff = "Anna"
#     movie_name = "Madagascar"
#     cs = CinemaHall(number)
#     clean = Cleaner(cleaning_staff)
#     some_customers = [
#         Customer(customer["name"], customer["food"])
#         for customer in customers
#     ]
#     cs.movie_session(movie_name, some_customers, clean)

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:

    def __init__(self, number: int):
        self.number = number

    def movie_session(self, movie_name: str, customers: Customer, cleaning_staff: Cleaner):
        print(f"\"Madagascar\" started in hall number {self.number}./n")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"\"Madagascar\" ended./n")
        cleaning_staff.clean_hall(self.number)



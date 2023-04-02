from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name: str, customers,
                      cleaning_staff):
        print(f'"{movie_name}" started in hall {self.number}.')
        Customer.watch_movie(customers, movie_name)
        print(f'"{movie_name}" ended')
        Cleaner.clean_hall(cleaning_staff, self.number)



# Cinema bar sold Coca-cola to Bob.
# Cinema bar sold popcorn to Alex.
# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.
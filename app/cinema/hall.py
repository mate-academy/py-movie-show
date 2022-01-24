from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f"\"{movie_name}\" started in hall number {self.number}.")
        for customer in customers:
            if not isinstance(customer, Customer):
                Customer.watch_movie(Customer(customer["name"],
                                              customer["food"]),
                                     movie_name)
            else:
                Customer.watch_movie(customer, movie_name)
        print(f"\"{movie_name}\" ended.")
        if not isinstance(cleaning_staff, Cleaner):
            return Cleaner(cleaning_staff).clean_hall(self.number)
        return cleaning_staff.clean_hall(self.number)

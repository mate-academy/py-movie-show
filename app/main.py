from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.customer import Customer
from people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    cinema_bar = CinemaBar()
    for customer in customers:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers, cleaner)

print("I am in main.py")
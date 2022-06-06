from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers = []
    for customer in customers:
        customers.append(Customer(customer["name"], customer["food"]))
    for customer in customers:
        bar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers, cleaner)

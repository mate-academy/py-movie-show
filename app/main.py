from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    ch = CinemaHall(hall_number)
    cb = CinemaBar()
    cl = Cleaner(cleaner)

    for customer in customers:
        cb.sell_product(customer, customer.food)
    ch.movie_session(movie, customers, cl)

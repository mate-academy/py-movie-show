from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cust = []
    for customer in customers:
        c = Customer(customer['name'], customer['food'])
        CinemaBar.sell_product(customer['food'], c)
        cust.append(c)

    cln = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, cust, cln)
    pass

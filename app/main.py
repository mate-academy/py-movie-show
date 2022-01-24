from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_of_customers = [Customer(visitor["name"], visitor["food"])
                         for visitor in customers]

    bar = CinemaBar()
    for hungry_soul in list_of_customers:
        bar.sell_product(hungry_soul, hungry_soul.food)

    CinemaHall(hall_number).movie_session(movie, list_of_customers,
                                          Cleaner(cleaner))

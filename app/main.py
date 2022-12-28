from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    instances = []
    cb = CinemaBar()
    for customer in customers:
        c = Customer(customer["name"], customer["food"])
        instances.append(c)
        cb.sell_product(c.food, c)
    ch = CinemaHall(hall_number)
    cl = Cleaner(cleaner)
    ch.movie_session(movie, instances, cl)

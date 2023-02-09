from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = []
    hall_cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    for person in customers:
        client = Customer(person["name"], person["food"])
        cinema_bar.sell_product(person["food"], client)
        customer_list.append(client)
    hall.movie_session(movie, customer_list, hall_cleaner)

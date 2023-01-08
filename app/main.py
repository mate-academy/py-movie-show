from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[Customer],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_ls = []
    for i in customers:
        customers_ls.append(Customer(i["name"], i["food"]))

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cinemas_clean = Cleaner(cleaner)

    for index in customers_ls:
        cinema_bar.sell_product(index.food, index)

    cinema_hall.movie_session(movie, customers_ls, cinemas_clean)

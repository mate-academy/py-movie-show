from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    cinemabar_list = []
    for customer in customers:
        cinemabar_list.append(Customer(customer["name"], customer["food"]))

    for cinemabar in cinemabar_list:
        print(CinemaBar.sell_product(cinemabar.food, cinemabar.name))

    CinemaHall.movie_session(movie, customers, cleaner)

    new_hall = CinemaHall(hall_number)
    new_cleaner = Cleaner(cleaner)
    print(new_hall.movie_session(movie, cinemabar_list, new_cleaner))

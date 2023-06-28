from __future__ import annotations

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        movie: str,
        customers: list[dict],
        hall_number: int,
        cleaner: str
) -> None:
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)

    customers_list = []
    for client in customers:
        new_customer = Customer(client["name"], client["food"])
        customers_list.append(new_customer)
        CinemaBar.sell_product(new_customer, new_customer.food)

    hall.movie_session(movie, customers_list, staff)

    #  staff.clean_hall(hall_number)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Joe", "food": "hamburger"},
    {"name": "Alex", "food": "popcorn"}
]

cleaner_name = "Anna"
hall_number = 5
cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="I'm robot")

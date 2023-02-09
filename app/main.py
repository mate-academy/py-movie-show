from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_list = []
    for i, customer in enumerate(customers):
        customers_list.append(
            Customer(customer["name"], customer["food"])
        )
        CinemaBar().sell_product(
            customers_list[i].food, customers_list[i]
        )
    CinemaHall(hall_number).movie_session(
        movie, customers_list, Cleaner(cleaner)
    )

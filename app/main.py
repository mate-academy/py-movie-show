from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for customer in customers:
        CinemaBar.sell_product(
            customer["food"],
            Customer(customer["name"], customer["food"])
        )

    customers_objects = []
    for customer in customers:
        customers_objects.append(Customer(customer["name"], customer["food"]))

    CinemaHall(hall_number).movie_session(
        movie,
        customers_objects,
        Cleaner(name=cleaner)
    )

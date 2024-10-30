from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import Any


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> Any:
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customer_objects = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, customer_objects, cleaning_staff)

    customer_instances = []
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customer_instances.append(customer)

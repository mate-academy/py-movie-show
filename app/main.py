from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from typing import List


def cinema_visit(
        customers: List[dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str) -> None:

    # Create instances of customers

    customers_instances = []
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        customers_instances.append(customer_instance)

    # Create instances of CinemaHall, CinemaBar and Cleaner
    hall = CinemaHall(hall_number)
    bar_clients = CinemaBar()
    cleaner = Cleaner(cleaning_staff)

    # Sell food to customers
    for person in customers_instances:
        bar_clients.sell_product(person, person.food)

    # Start movie session
    hall.movie_session(movie_name, customers_instances, cleaner)

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaning_staff: str, movie_name: str) -> None:
    customer_instances = []
    cb = CinemaBar()
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        customer_instances.append(new_customer)
        cb.sell_product(customer["food"], new_customer)
    CinemaHall(hall_number).movie_session(movie_name, customer_instances, Cleaner(cleaning_staff))

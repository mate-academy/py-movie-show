from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int, cleaner, movie: str):
    customer_instances = []
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        customer_instances.append(customer_instance)
        CinemaBar.sell_product(customer_instance, customer["food"])
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    CinemaHall.movie_session(hall, movie, customer_instances, staff)

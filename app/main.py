from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customer_instances = []
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        customer_instances.append(customer_instance)
    hall = CinemaHall(hall_number)
    bar = CinemaBar()
    cleaner_instance = Cleaner(cleaner)
    for customer in customer_instances:
        bar.sell_product(customer.food, customer)
    hall.movie_session(movie, customer_instances, cleaner_instance)

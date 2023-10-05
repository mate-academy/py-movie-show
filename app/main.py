from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    bar_instances = CinemaBar()

    customers_instances = []
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        bar_instances.sell_product(customer["food"], customer_instance)
        customers_instances.append(customer_instance)

    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_instances, cleaner)

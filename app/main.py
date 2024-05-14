from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customers_instances = [
        Customer(customer['name'], customer['food']) for customer in customers
    ]
    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()

    for customer in customers_instances:
        bar_instance.sell_product(customer, customer.food)

    hall_instance.movie_session(movie, customers_instances, cleaner_instance)

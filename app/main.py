from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_instance, customer["food"])

    cleaning = Cleaner(name=cleaner)
    cinema_instance = CinemaHall(hall_number)
    customer_instance = []
    for customer in customers:
        customer_instance.append(Customer(customer["name"], customer["food"]))

    CinemaHall.movie_session(cinema_instance, movie, customer_instance,
                             cleaning)


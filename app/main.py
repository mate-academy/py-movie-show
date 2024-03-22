from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_arr = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customer_arr.append(customer_obj)
        CinemaBar().sell_product(customer_obj, customer_obj.food)
    CinemaHall.movie_session(CinemaHall(hall_number),
                             movie, customer_arr, Cleaner(cleaner))

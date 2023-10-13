from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    cinema_hall_instance = CinemaHall(hall_number)
    customer_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in customer_list:
        CinemaBar.sell_product(customer, customer.food)
    cinema_hall_instance.movie_session(movie, customer_list, Cleaner(cleaner))

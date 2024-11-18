from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:  # NOQA E501
    customers_objects = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]  # NOQA E501
    for customer in customers_objects:
        CinemaBar().sell_product(product=customer.food, customer=customer)
    clean = Cleaner(name=cleaner)
    CinemaHall(number=hall_number).movie_session(
        movie_name=movie, customer=customers_objects, cleaning_staff=clean  # NOQA E501
    )  # NOQA E501
    pass # NOQA E501

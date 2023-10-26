from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = []
    for new_customer in customers:
        person = Customer(new_customer["name"], new_customer["food"])
        list_of_customers.append(person)
        CinemaBar.sell_product(new_customer["food"], person)
    CinemaHall.movie_session(
        CinemaHall(hall_number),
        movie, list_of_customers,
        Cleaner(cleaner)
    )

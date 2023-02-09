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
    clients = []

    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        clients.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    CinemaHall.movie_session(
        CinemaHall(hall_number),
        movie_name=movie,
        customers=clients,
        cleaning_staff=Cleaner(cleaner)
    )

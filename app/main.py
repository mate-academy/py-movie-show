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
    cleaner = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)

    customers = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]

    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)

    hall_number.movie_session(movie, customers, cleaner)

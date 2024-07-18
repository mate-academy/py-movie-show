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
    cb = CinemaBar()
    ch = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers_list:
        cb.sell_product(customer.food, customer.name)

    ch.movie_session(movie, customers_list, staff)

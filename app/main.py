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
    c_staff = Cleaner(cleaner)
    for customer in customers:
        customer["name"] = Customer(customer["name"], customer["food"])
        list_of_customers.append(customer["name"])
        CinemaBar.sell_product(customer["name"], customer["name"].food)
    CinemaHall.movie_session(
        CinemaHall(hall_number),
        movie,
        list_of_customers,
        c_staff
    )

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
    cleaner_instance = Cleaner(cleaner)

    for cust in customers:
        customer_instance = Customer(cust["name"], cust["food"])
        cb.sell_product(customer_instance, customer_instance.food)

    ch.movie_session(
        movie,
        [Customer(cust["name"], cust["food"]) for cust in customers],
        cleaner_instance,
    )

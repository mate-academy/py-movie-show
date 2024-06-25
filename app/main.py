from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cb = CinemaBar()
    ch = CinemaHall(hall_number)

    customers_as_classes = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cleaner_as_class = Cleaner(cleaner)

    for customer in customers_as_classes:
        cb.sell_product(customer=customer, product=customer.food)

    ch.movie_session(movie_name=movie,
                     customers=customers_as_classes,
                     cleaning_staff=cleaner_as_class)

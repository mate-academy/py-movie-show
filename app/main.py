from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers = [
        Customer(name=client["name"], food=client["food"])
        for client in customers
    ]
    ch = CinemaHall(number=hall_number)
    cb = CinemaBar()
    cleaner = Cleaner(name=cleaner)

    for customer in customers:
        cb.sell_product(customer=customer, product=customer.food)

    ch.movie_session(movie_name=movie,
                     customers=customers,
                     cleaning_staff=cleaner)

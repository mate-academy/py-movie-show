from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = [Customer(customer["name"],
                          customer["food"]) for customer in customers]

    cinka = CinemaBar()
    for customer in customer_instances:
        cinka.sell_product(customer, customer.food)

    movki = CinemaHall(hall_number)
    cleanki = Cleaner(cleaner)
    movki.movie_session(movie, customer_instances, cleanki)

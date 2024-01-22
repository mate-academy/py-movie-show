from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_instances = []
    for customer in customers:
        customers_instances.append(Customer(name=customer["name"],
                                            food=customer["food"]))
    CinemaBar()
    for customer in customers_instances:
        CinemaBar.sell_product(customer, customer.food)
    CinemaHall(hall_number).movie_session(movie_name=movie,
                                          customers=customers_instances,
                                          cleaning_staff=Cleaner(cleaner))

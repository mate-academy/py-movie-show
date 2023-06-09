from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    visitors = []
    for visitor in customers:
        visitors.append(Customer(visitor["name"], visitor["food"]))
        CinemaBar.sell_product(Customer(visitor["name"], visitor["food"]),
                               Customer(visitor["name"], visitor["food"]).food)
    CinemaHall(hall_number).movie_session(movie,
                                          visitors,
                                          Cleaner(cleaner))

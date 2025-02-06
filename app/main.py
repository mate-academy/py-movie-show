from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    for customer in customers:
        CinemaBar.sell_product(customer["name"], customer["food"])
    clean = Cleaner(cleaner)
    num = CinemaHall(hall_number)
    CinemaHall.movie_session(self=num,
                             movie_name=movie,
                             customers=[Customer(customer["name"],
                                                 customer["food"])
                                        for customer in customers],
                             cleaning_staff=clean)

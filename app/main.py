from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    CinemaBar()
    for customer in customers:
        CinemaBar.sell_product(
            Customer(customer["name"],
                     customer["food"]),
            customer["food"])
    CinemaHall.movie_session(
        CinemaHall(hall_number), movie,
        [Customer(customer["name"],
         customer["food"]) for customer in customers],
        Cleaner(cleaner))

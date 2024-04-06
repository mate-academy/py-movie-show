from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    visitors = []
    for customer in customers:
        visitor = Customer(customer["name"], customer["food"])
        visitors.append(visitor)

    hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    for visitor in visitors:
        CinemaBar.sell_product(visitor, visitor.food)

    hall.movie_session(movie, visitors, cinema_cleaner)

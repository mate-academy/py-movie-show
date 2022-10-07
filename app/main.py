from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    visitors = []
    for customer in customers:
        visitor = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(visitor.food, visitor)
        visitors.append(visitor)

    cleaner = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, visitors, cleaner)

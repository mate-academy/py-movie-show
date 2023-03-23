from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cb = CinemaBar()

    cinema_customers = [Customer(customer["name"], customer["food"])
                        for customer in customers]

    cinema_cleaner = Cleaner(cleaner)

    for cinema_customer in cinema_customers:
        cb.sell_product(cinema_customer, cinema_customer.food)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, cinema_customers, cinema_cleaner)

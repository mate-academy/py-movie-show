from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_customers = [Customer(**customer) for customer in customers]
    cinema_cleaner = Cleaner(cleaner)
    for cinema_customer in cinema_customers:
        cinema_bar.sell_product(cinema_customer.food, cinema_customer)
    cinema_hall.movie_session(movie, cinema_customers, cinema_cleaner)

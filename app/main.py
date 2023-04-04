from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)

    for customer in customers:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(
        movie,
        [Customer(**customer) for customer in customers],
        cleaner_name
    )

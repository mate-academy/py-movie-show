from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cb = CinemaBar()

    cinema_customers = []
    for customer in customers:
        cinema_customers.append(Customer(customer["name"], customer["food"]))

    cinema_cleaner = Cleaner(cleaner)

    for cinema_customer in cinema_customers:
        cb.sell_product(cinema_customer, cinema_customer.food)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, cinema_customers, cinema_cleaner)

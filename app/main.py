from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hull_number: int,
                 cleaner: str, movie: str) -> None:
    customers_save = [Customer(customer["name"], customer["food"])
                      for customer in customers]

    cinema_hall, cinema_bar, hall_cleaner = \
        CinemaHall(hull_number), CinemaBar(), Cleaner(cleaner)

    for customer in customers_save:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customers_save, hall_cleaner)

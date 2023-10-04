from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instance = [Customer(customer.get("name"),
                                   customer.get("food"))
                          for customer in customers]
    cleaner_instance = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()

    for customer in customers_instance:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, customers_instance, cleaner_instance)

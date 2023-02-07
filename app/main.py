from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    custom_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    clean_person = Cleaner(cleaner)
    for customer in custom_instances:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, custom_instances, clean_person)

from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> str:
    customers_objects = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    [
        CinemaBar.sell_product(customer, customer.food)
        for customer in customers_objects
    ]

    hall = CinemaHall(hall_number)
    cleaning = Cleaner(cleaner)
    hall.movie_session(movie, customers_objects, cleaning)

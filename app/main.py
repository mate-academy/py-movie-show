from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[Customer], hall_number: int, cleaner: str, movie: str) -> None:
    for person in customers:
        customer = Customer(person["name"], person["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
    cleaner_name = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=cleaner_name)

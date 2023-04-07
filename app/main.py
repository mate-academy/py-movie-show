from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cleaner = Cleaner(cleaner)
    customers_inst = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    for customer in customers_inst:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customers_inst, cleaner)

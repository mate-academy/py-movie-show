from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    result = []
    for person in customers:
        customer = Customer(person["name"], person["food"])
        result.append(customer)
        CinemaBar.sell_product(customer=customer, product=customer.food)
    CinemaHall(hall_number).movie_session(movie, result, Cleaner(cleaner))

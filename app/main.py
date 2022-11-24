from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    custom_list = [
        Customer(guest["name"], guest["food"])
        for guest in customers]
    for person in custom_list:
        CinemaBar.sell_product(
            customer=person,
            product=person.food)
    CinemaHall(hall_number).movie_session(movie, custom_list, Cleaner(cleaner))

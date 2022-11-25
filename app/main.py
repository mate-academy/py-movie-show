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
<<<<<<< HEAD
    cb = CinemaBar()
    for person in custom_list:
        cb.sell_product(
=======
    for person in custom_list:
        CinemaBar.sell_product(
>>>>>>> 8a0cf225de1c1d9d1123ba0233a2f852bd01be29
            customer=person,
            product=person.food)
    CinemaHall(hall_number).movie_session(movie, custom_list, Cleaner(cleaner))

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

    custom_list_inst = []
    for pers in customers:
        custom_pers_inst = Customer(pers.get("name"), pers.get("food"))
        custom_list_inst.append(custom_pers_inst)

    c_hall_inst = CinemaHall(hall_number)
    bar_cinema = CinemaBar()

    cleaner_instance = Cleaner(cleaner)

    for pers in custom_list_inst:
        bar_cinema.sell_product(pers, pers.food)

    c_hall_inst.movie_session(movie, custom_list_inst, cleaner_instance)

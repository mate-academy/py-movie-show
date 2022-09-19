from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    cust_inst = []

    for person in customers:
        pers = Customer(person["name"], person["food"])
        cust_inst.append(pers)
        obj = CinemaBar()
        obj.sell_product(pers.food, pers)

    hl = CinemaHall(hall_number)
    cln = Cleaner(cleaning_staff)
    hl.movie_session(movie_name, cust_inst, cln)

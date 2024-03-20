from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    total = []
    for cust in customers:
        inst = Customer(cust["name"], cust["food"])
        total.append(inst)
    inst_c_h = CinemaHall(hall_number)
    inst_c_b = CinemaBar()
    inst_cl = Cleaner(cleaner)
    for cust in total:
        inst_c_b.sell_product(cust.food, cust)
    inst_c_h.movie_session(movie, total, inst_cl)

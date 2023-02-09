from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    ls_inst_customers = []
    for info in customers:
        ls_inst_customers.append(Customer(info["name"], info["food"]))

    inst_cinema = CinemaHall(hall_number)
    inst_cleaner = Cleaner(cleaner)
    inst_cinema_bar = CinemaBar()

    for person in customers:
        inst_customer = Customer(person["name"], person["food"])
        inst_cinema_bar.sell_product(person["food"], inst_customer)

    inst_cinema.movie_session(movie, ls_inst_customers, inst_cleaner)

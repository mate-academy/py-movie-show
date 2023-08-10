from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str,
) -> None:
    for visitor in customers:
        person = Customer(visitor["name"], visitor["food"])
        product = visitor["food"]
        CinemaBar.sell_product(product, person)

    # hall_num = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)
    CinemaHall(hall_number).movie_session(movie_name, customers, cleaner)

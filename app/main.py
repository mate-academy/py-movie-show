from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:

    customer_list = []
    for index in customers:
        customer = Customer(index["name"], index["food"])
        customer_list.append(customer)
        CinemaBar.sell_product(customer=customer, product=index["food"])

    clean = Cleaner(name=cleaner)
    cinema = CinemaHall(number=hall_number)
    cinema.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=clean,
    )

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    cust = []
    for customer in customers:
        cust.append(Customer(customer["name"], customer["food"]))
        CinemaBar.sell_product(
            Customer(customer["name"],
                     customer["food"]),
            customer["food"])

    cinema.movie_session(movie, cust, clean)

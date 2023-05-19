from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cb = CinemaBar
    cleaner = Cleaner(cleaner)
    ch = CinemaHall(hall_number)
    customers = {
        customer["name"]: Customer(
            customer["name"],
            customer["food"]
        )
        for customer in customers
    }
    for customer in customers.values():
        cb.sell_product(customer.food, customer)
    ch.movie_session(movie, list(customers.values()), cleaner)

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_arr = list(map(lambda customer: Customer(
        customer["name"], customer["food"]), customers))
    [CinemaBar.sell_product(customer,
                            customer.food) for customer in customer_arr]
    CinemaHall.movie_session(CinemaHall(hall_number),
                             movie, customer_arr, Cleaner(cleaner))

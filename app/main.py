from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:
    customers_info = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    hall_num = CinemaHall(hall_number)
    bar = CinemaBar()
    worker = Cleaner(cleaner)

    for customer in customers_info:
        bar.sell_product(customer.food, customer)

    hall_num.movie_session(movie, customers_info, worker)

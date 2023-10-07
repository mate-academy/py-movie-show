from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    customers_inst = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    hall = CinemaHall(hall_number)
    bar = CinemaBar()
    cleaner = Cleaner(cleaning_staff)

    for customer in customers_inst:
        bar.sell_product(customer.food, customer)

    hall.movie_session(movie_name, customers_inst, cleaner)

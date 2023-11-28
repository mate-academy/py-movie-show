from app.cinema.bar import CinemaBar
from app.cinema.customer import Customer
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customer_list = []
    for index, value in enumerate(customers):
        customer = Customer(value["name"], value["food"])
        customer_list.append(customer)
        CinemaBar.sell_product(value["food"], customer)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_list, cleaner)

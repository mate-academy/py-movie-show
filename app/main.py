from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cinema_staff = Cleaner(cleaning_staff)
    customer_list = []

    for customer in customers:
        visitor = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(customer=visitor, product=visitor.food)
        customer_list.append(visitor)

    hall.movie_session(movie_name, customer_list, cinema_staff)

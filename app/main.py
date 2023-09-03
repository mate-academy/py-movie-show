from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        movie_name: str,
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    customers_info = []

    for costumer in customers:
        name = costumer["name"]
        food = costumer["food"]

        customer = Customer(name, food)
        customers_info.append(costumer)

    for customer in customers_info:
        cinema_bar.sell_product(customer.name, costumer.food)

    cinema_hall.movie_session(movie_name, costumers_info, cleaner)

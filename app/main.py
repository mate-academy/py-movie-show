from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = []

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer in customers:
        customer_add = Customer(customer["name"], customer["food"])
        customers_list.append(customer_add)
        cinema_bar.sell_product(customer_add.food, customer_add)

    cinema_hall.movie_session(movie, customers_list, cleaning_staff)

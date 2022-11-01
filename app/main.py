from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))

    for customer_instance in customer_list:
        CinemaBar.sell_product(customer_instance.food, customer_instance)

    new_hall_number = CinemaHall(hall_number)
    new_cleaner = Cleaner(cleaner)
    new_hall_number.movie_session(movie, customer_list, new_cleaner)

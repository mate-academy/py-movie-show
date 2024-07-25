from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_inst_list = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    cineme_hall_inst = CinemaHall(hall_number)
    cinema_bar_inst = CinemaBar()
    cleaner_inst = Cleaner(cleaner)

    for customer in customers_inst_list:
        cinema_bar_inst.sell_product(customer.food, customer)

    cineme_hall_inst.movie_session(movie, customers_inst_list, cleaner_inst)

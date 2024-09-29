from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    for customer in customers:
        customers_list.append(Customer(customer["name"], customer["food"]))
    cleaner_obj = Cleaner(cleaner)
    hall_obj = CinemaHall(hall_number)
    bar_obj = CinemaBar()
    for customer_obj in customers_list:
        bar_obj.sell_product(customer_obj.food, customer_obj)
    hall_obj.movie_session(movie, customers_list, cleaner_obj)

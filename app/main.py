from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list: list[Customer] = [
        Customer(current["name"], current["food"]) for current in customers
    ]
    cinema_hall: CinemaHall = CinemaHall(hall_number)
    cleaner: Cleaner = Cleaner(cleaner)
    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, customers_list, cleaner)

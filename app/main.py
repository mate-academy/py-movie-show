# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    for i in range(len(customers_list)):
        CinemaBar.sell_product(customers_list[i].food, customers_list[i])
    hall_number = CinemaHall(hall_number)
    hall_number.movie_session(movie, customers_list, Cleaner(cleaner))

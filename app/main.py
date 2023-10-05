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
        Customer(
            item.get("name"),
            item.get("food")
        )
        for item in customers
    ]
    hall_cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()

    for customer in customers_list:
        cinema_bar.sell_product(customer, customer.food)

    hall.movie_session(movie, customers_list, hall_cleaner)

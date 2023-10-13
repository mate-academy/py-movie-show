from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(
        movie,
        [
            Customer(customer_info["name"], customer_info["food"])
            for customer_info in customers
        ],
        cinema_cleaner
    )

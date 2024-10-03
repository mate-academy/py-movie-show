import warnings
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie_title: str,
        customers_list: list[dict[str, str]],
        hall_id: int,
        cleaner_name: str
) -> None:
    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers_list
    ]
    cinema_hall = CinemaHall(hall_id)
    cinema_bar = CinemaBar()
    cleaner_instance = Cleaner(cleaner_name)
    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(
        movie_title,
        customer_instances,
        cleaner_instance
    )


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name_outer = "Anna"
movie = "Madagascar"
cinema_visit(movie, customers, hall_number, cleaner_name_outer)

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pytest")

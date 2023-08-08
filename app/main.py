from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customers_instances = []

    for customer in customers:
        customers_instances.append(
            Customer(
                customer["name"],
                customer["food"]
            )
        )

    cinema_hall_inst = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_inst = Cleaner(cleaner)

    for customer in customers_instances:
        cinema_bar.sell_product(
            customer.food, customer.name
        )

    cinema_hall_inst.movie_session(
        movie, customers_instances, cleaner_inst
    )

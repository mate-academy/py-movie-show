from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_instance = [
        Customer(
            name=element.get("name"),
            food=element.get("food")
        ) for element in customers
    ]
    hall_instance = CinemaHall(
        number=hall_number
    )
    cleaner_instance = Cleaner(
        name=cleaner
    )
    bar_instance = CinemaBar()

    for customer in customers_instance:
        bar_instance.sell_product(customer.food, customer)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customers_instance,
        cleaning_staff=cleaner_instance
    )

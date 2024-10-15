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
    customer_instances = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        ) for customer in customers
    ]

    hall_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()
    cleaner_instance = Cleaner(cleaner)

    for customer in customer_instances:
        bar_instance.sell_product(customer=customer, product=customer.food)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )

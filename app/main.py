from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie_name: str
) -> None:
    customer_objects = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        )
        for customer in customers
    ]

    cinema_bar = CinemaBar()

    for customer in customer_objects:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(number=hall_number)

    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie_name,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )

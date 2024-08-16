from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cleaner_instance = Cleaner(name=cleaner)
    customer_instances = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()

    for person in customer_instances:
        cinema_bar.sell_product(
            product=person.food,
            customer=person
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance,
    )

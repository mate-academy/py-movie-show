from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List, Dict


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int,
        cleaner: str, movie: str
) -> None:
    customer_objects = [
        Customer(name=customer["name"],
                 food=customer["food"]
                 ) for customer in customers
    ]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_object = Cleaner(name=cleaner)

    for customer in customer_objects:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_object
    )

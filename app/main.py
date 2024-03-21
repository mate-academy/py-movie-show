from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int,
                 cleaner_name: str,
                 movie: str) -> None:
    cb = CinemaBar()
    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner_name)

    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])
        cb.sell_product(customer, customer.food)

    hall.movie_session(movie_name=movie,
                       customers=[Customer
                                  (name=customer_data["name"],
                                   food=customer_data["food"])
                                  for customer_data in customers],
                       cleaning_staff=cleaner)

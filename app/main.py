from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie_name: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    customer_instances = []

    for customer in customers:
        customer_instance = Customer(name=customer["name"],
                                     food=customer["food"])
        customer_instances.append(customer_instance)
        cinema_bar.sell_product(product=customer_instance.food,
                                customer=customer_instance)

    cinema_hall.movie_session(movie_name=movie_name,
                              customers=customer_instances,
                              cleaning_staff=cleaner_instance)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers,
             hall_number=5,
             cleaner="Anna",
             movie_name="Madagascar")

from typing import List
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List,
                 hall_number: int,
                 cleaner_name: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner_name)

    for customer_info in customers:
        customer = Customer(name=customer_info["name"],
                            food=customer_info["food"])
        cinema_bar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=[Customer(name=customer["name"],
                            food=customer["food"]) for customer in customers],
        cleaning_staff=cleaner
    )


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"

cinema_visit(customers=customers,
             hall_number=hall_number,
             cleaner_name=cleaner_name,
             movie=movie)

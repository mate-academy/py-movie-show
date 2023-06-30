from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from typing import List


def cinema_visit(
        customers: List[dict],
        hall_number: int,
        cleaner_name: str,
        movie_name: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner_name)

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(movie_name=movie_name,
                              customers=[
                                  Customer(**customer)
                                  for customer in customers
                              ],
                              cleaning_staff=cleaning_staff)

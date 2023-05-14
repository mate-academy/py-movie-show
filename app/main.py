from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    ls_customers = [Customer(one_customer["name"], one_customer["food"])
                    for one_customer in customers]

    hall = CinemaHall(hall_number)

    cleaner_hall = Cleaner(cleaner)

    for one_customer in ls_customers:
        CinemaBar.sell_product(
            product=one_customer.food,
            customer=one_customer
        )

    CinemaHall.movie_session(self=hall,
                             movie_name=movie,
                             customers=ls_customers,
                             cleaning_staff=cleaner_hall)

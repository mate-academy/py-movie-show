from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    ls_customers = []

    for one_customer in customers:
        ls_customers.append(Customer(
            name=one_customer["name"],
            food=one_customer["food"]
        ))

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

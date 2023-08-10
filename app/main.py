from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_objs = []

    for customer in customers:
        customers_objs.append(Customer(
            name=customer["name"],
            food=customer["food"]))

    cleaner_obj = Cleaner(cleaner)

    for customer in customers_objs:
        CinemaBar.sell_product(
            customer=customer,
            product=customer.food)

    cinema_hall = CinemaHall(hall_number)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_objs,
        cleaning_staff=cleaner_obj)

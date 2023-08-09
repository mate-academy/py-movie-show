from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str)\
        -> None:

    all_customers = []

    for curr_customer in customers:
        all_customers.append(Customer(
            name=curr_customer["name"],
            food=curr_customer["food"]))

    curr_cleaner = Cleaner(cleaner)

    for curr_customer in all_customers:
        CinemaBar.sell_product(
            customer=curr_customer,
            product=curr_customer.food)

    cur_hall = CinemaHall(hall_number)

    cur_hall.movie_session(
        movie_name=movie,
        customers=all_customers,
        cleaning_staff=curr_cleaner)

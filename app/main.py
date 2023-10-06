from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    updated_customers = []

    for customer in customers:
        new_customer = Customer(customer.get("name"), customer.get("food"))

        updated_customers.append(new_customer)

    for customer in updated_customers:
        CinemaBar.sell_product(customer, customer.food)

    updated_cleaner = Cleaner(cleaner)

    CinemaHall(hall_number).movie_session(movie,
                                          updated_customers,
                                          updated_cleaner)

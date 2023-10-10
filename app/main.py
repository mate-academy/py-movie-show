# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_objects = []
    cinema_session = CinemaHall(hall_number)
    staff = Cleaner(cleaner)

    for customer in customers:
        customer_objects.append(
            Customer(customer.get("name"), customer.get("food"))
        )

    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    cinema_session.movie_session(movie, customer_objects, staff)

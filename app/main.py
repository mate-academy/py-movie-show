from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_inst = []

    for person in customers:
        person_obj = Customer(
            person["name"],
            person["food"]
        )
        customer_inst.append(person_obj)

    cleaner_inst = Cleaner(cleaner)

    for customer in customer_inst:
        CinemaBar.sell_product(customer, customer.food)

    CinemaHall(hall_number).movie_session(movie, customer_inst, cleaner_inst)

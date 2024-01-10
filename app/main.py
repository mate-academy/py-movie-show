from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer.food, customer)
        list_of_customers.append(customer)
    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=Cleaner(cleaner)
    )

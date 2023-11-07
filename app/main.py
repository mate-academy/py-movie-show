from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    list_off_customers = []
    for customer in customers:
        list_off_customers.append(Customer(customer["name"], customer["food"]))
    customers = list_off_customers

    for customer in customers:
        CinemaBar.sell_product(customer, customer)

    cleaning_staff = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)

    CinemaHall.movie_session(
        hall_number,
        movie_name=movie,
        customers=customers,
        cleaning_staff=cleaning_staff
    )

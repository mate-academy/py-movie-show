from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_num: int, clean: str, mov: str) -> None:
    Customer.customers = []
    staff = Cleaner(name=clean)
    hall = CinemaHall(hall_num)

    for client in customers:

        customer = Customer(name=client["name"], food=client["food"])
        CinemaBar.sell_product(customer, customer.food)

    hall.movie_session(mov, Customer.customers, staff)

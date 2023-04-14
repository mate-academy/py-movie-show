from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    customers_list = []
    staff = Cleaner(cleaner)
    for customer in customers:
        customer = Customer(
            name=customer.get("name"),
            food=customer.get("food")
        )
        CinemaBar.sell_product(customer.food, customer)
        customers_list.append(customer)
    CinemaHall.movie_session(CinemaHall(hall_number),
                             movie_name=movie,
                             customers=customers_list,
                             cleaning_staff=staff)

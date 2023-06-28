from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    list_of_customer = []
    for cust in customers:
        customer = Customer(cust["name"], cust["food"])
        list_of_customer.append(customer)
        CinemaBar.sell_product(product=cust["food"], customer=customer)

    if type(cleaner) is Cleaner:
        CinemaHall(hall_number).movie_session(
            movie,
            list_of_customer,
            cleaner.name
        )
    else:
        CinemaHall(hall_number).movie_session(
            movie,
            list_of_customer,
            cleaner
        )

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:

    for cust in customers:
        customer = Customer(cust["name"], cust["food"])
        CinemaBar.sell_product(product=cust["food"], customer=customer)

    CinemaHall(hall_number).movie_session(movie, customers, cleaner)

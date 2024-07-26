from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    cinema_bar = CinemaBar()
    customers_list = []
    for cust in customers:
        customer = Customer(name=cust["name"], food=cust["food"])
        cinema_bar.sell_product(product=cust["food"], customer=customer)
        customers_list.append(customer)

    cinema_hall = CinemaHall(number=hall_number)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customers_list,
                              cleaning_staff=Cleaner(name=cleaner))

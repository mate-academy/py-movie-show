from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cust_list = []
    for customer in customers:
        client = Customer(customer["name"], customer["food"])
        cust_list.append(client)
        CinemaBar.sell_product(product=customer["food"], customer=client)

    cleaner = Cleaner(cleaner)
    num_hall = CinemaHall(hall_number)
    CinemaHall.movie_session(num_hall, movie, cust_list, cleaner)

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinima_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    customer_instances = []
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        cinima_bar.sell_product(product=cust.food, customer=cust)
        customer_instances.append(cust)

    hall.movie_session(movie_name=movie,
                       customers=customer_instances,
                       cleaning_staff=cleaning_staff)

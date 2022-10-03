from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_obj = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customers_obj.append(customer_obj)
        CinemaBar.sell_product(product=customer_obj.food,
                               customer=customer_obj)

    hall = CinemaHall(hall_number)
    CinemaHall.movie_session(hall,
                             movie_name=movie,
                             customers=customers_obj,
                             cleaning_staff=Cleaner(cleaner))

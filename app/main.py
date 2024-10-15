from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    numb_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers_inst_list = []
    for customer in customers:
        customer_each = Customer(customer["name"], customer["food"])
        customers_inst_list.append(customer_each)
        CinemaBar.sell_product(customer=customer_each,
                               product=customer_each.food)
    CinemaHall.movie_session(self=numb_hall,
                             movie_name=movie,
                             customers=customers_inst_list,
                             cleaning_staff=cleaner)

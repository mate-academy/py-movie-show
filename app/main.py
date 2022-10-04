from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str):
    list_of_customers = [Customer(customer["name"],
                                  customer["food"]) for customer in customers]
    number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in list_of_customers:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    CinemaHall.movie_session(number, movie, list_of_customers, cleaner)

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    all_customers = []
    for customer in customers:
        all_customers.append(Customer(name=customer["name"],
                                      food=customer["food"]))
    CinemaBar()
    for customer in all_customers:
        CinemaBar.sell_product(customer, customer.food)
    CinemaHall(hall_number).movie_session(movie_name=movie,
                                          customers=all_customers,
                                          cleaning_staff=Cleaner(cleaner))

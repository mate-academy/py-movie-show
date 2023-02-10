from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = [
        Customer(name=customer.get("name"), food=customer.get("food"))
        for customer in customers
    ]
    hall = CinemaHall(hall_number)
    clean_stuff = Cleaner(cleaner)
    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers_list, clean_stuff)

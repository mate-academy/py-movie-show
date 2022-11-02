from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> str:
    custom_inst = [Customer(cust["name"], cust["food"]) for cust in customers]
    cinema_hall = CinemaHall(hall_number)
    c_bar = CinemaBar()
    clean_person = Cleaner(cleaner)
    for customer in custom_inst:
        c_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, custom_inst, clean_person)

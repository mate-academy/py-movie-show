from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer_dict in customers:
        customer = Customer(customer_dict['name'], customer_dict['food'])
        bar.sell_product(customer, customer.food)

    hall.movie_session(movie, [Customer(c['name'], c['food']) for c in customers], cleaner)

from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    worker = Cleaner(cleaner)
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        bar.sell_product(customer, customer.food)
    hall.movie_session(movie, Customer.people, worker)

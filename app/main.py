from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    Cleaner(cleaner)
    number = 0
    for _ in customers:
        customer_name = customers[number]['name']
        customer_food = customers[number]['food']
        Customer(customer_name, customer_food)
        CinemaBar.sell_product(customer_food, customer_name)
        number += 1
    session = CinemaHall(hall_number)
    session.movie_session(movie_name=movie, customers=customers, cleaning_staff=cleaner)

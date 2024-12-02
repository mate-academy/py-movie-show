from __future__ import annotations
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    peoples = []
    for customer in customers:
        peoples.append(Customer(customer["food"], customer["name"]))

    for people in peoples:
        CinemaBar.sell_product(people.name, people.food)
    cleaner_for_cinema = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, peoples, cleaner_for_cinema)

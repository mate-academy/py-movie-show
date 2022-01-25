from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    listOfInstances = []
    for customer in customers:
        listOfInstances.append(Customer(customer["name"], customer["food"]))
        CinemaBar.sell_product(Customer(customer["name"],
                                        customer["food"]),
                               Customer(customer["name"],
                                        customer["food"]).food)
    cleaner_guy = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, listOfInstances, cleaner_guy)

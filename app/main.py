import sys
from importlib import import_module

sys.path.insert(0, "..")

# import modules
CinemaBar = import_module("app.cinema.bar").CinemaBar
CinemaHall = import_module("app.cinema.hall").CinemaHall
Customer = import_module("app.people.customer").Customer
Cleaner = import_module("app.people.cinema_staff").Cleaner


def cinema_visit(customers, hall_number, cleaner_name, movie):
    cb = CinemaBar()
    ch = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    customer_instances = [Customer(c["name"], c["food"]) for c in customers]

    for customer in customer_instances:
        cb.sell_product(customer, customer.food)

    ch.movie_session(movie, customer_instances, cleaner)

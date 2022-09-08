from people.customer import Customer
from cinema.hall import CinemaHall
from people.cinema_staff import Cleaner
from cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    new_customers = []
    bar = CinemaBar()
    for i in customers:
        new_customer = Customer(i["name"], i["food"])
        new_customers.append(new_customer)
        bar.sell_product(new_customer.food, new_customer.name)
    hall = CinemaHall(hall_number)
    hall_clean = Cleaner(cleaner)
    hall.movie_session(movie, new_customers, hall_clean)

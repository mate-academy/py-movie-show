from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    lst = []
    for item in customers:
        customer = Customer(item["name"], item["food"])
        lst.append(customer)
        bar = CinemaBar()
        bar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, lst, cleaning_staff)

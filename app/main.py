from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    cinema_bar = CinemaBar()
    for customer in customers:
        customer_in_list = Customer(customer["name"], customer["food"])
        customers_list.append(customer_in_list)
        cinema_bar.sell_product(customer_in_list.food, customer_in_list)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, customers_list, cleaning_staff)

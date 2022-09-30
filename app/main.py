from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_obj = []
    for customer in customers:
        customers_obj.append(Customer(customer["name"], customer["food"]))
    for i in customers_obj:
        CinemaBar.sell_product(product=i.food, customer=i)
    hall = CinemaHall(hall_number)
    CinemaHall.movie_session(hall,
                             movie_name=movie,
                             customers=customers_obj,
                             cleaning_staff=Cleaner(cleaner))

from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = [Customer(customer["name"], customer["food"])
                      for customer in customers]

    cb = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_stuff = Cleaner(cleaner)

    for customer in customers_list:
        cb.sell_product(customer.food, customer)

    hall.movie_session(movie, customers_list, cleaner_stuff)

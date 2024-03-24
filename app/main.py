from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    customers_list = [Customer(name=c["name"], food=c["food"])
                      for c in customers]

    for customer in customers_list:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customers_list, cleaner)

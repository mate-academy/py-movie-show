from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    bar_cinema = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        bar_cinema.sell_product(customer.food, customer,)

    hall.movie_session(movie,
                       [Customer(customer["name"],
                                 customer["food"])
                        for customer in customers],
                       cleaner_instance)

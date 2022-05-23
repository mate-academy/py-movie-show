from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        visitors: list,
        hall_number: int,
        cleaner_name: str,
        movie: str
):

    hall = CinemaHall(hall_number)
    bar = CinemaBar()
    cleaner = Cleaner(cleaner_name)
    customers = [
        Customer(visitor["name"], visitor["food"])
        for visitor in visitors
    ]

    for customer in customers:
        bar.sell_product(customer, customer.food)

    hall.movie_session(movie, customers, cleaner)

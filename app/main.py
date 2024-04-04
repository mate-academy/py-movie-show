from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    list_of_a_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cb = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_stuff = Cleaner(cleaner)

    for customer in list_of_a_customers:
        cb.sell_product(customer.food, customer)

    hall.movie_session(movie, list_of_a_customers, cleaner_stuff)

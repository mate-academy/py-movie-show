from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_customers = []
    for customer in customers:
        cinema_customers.append(Customer(customer["name"], customer["food"]))

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for cinema_customer in cinema_customers:
        cinema_bar.sell_product(cinema_customer.food, cinema_customer)

    cinema_hall.movie_session(movie, cinema_customers, cleaner)

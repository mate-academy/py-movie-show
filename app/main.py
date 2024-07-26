from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    # create Customers instances
    customers_obj = []
    for customer in customers:
        customers_obj.append(Customer(customer["name"], customer["food"]))

    # create CinemaHall, CinemaBar, and Cleaner instances
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_staff = Cleaner(cleaner)

    # sell food to customers
    for customer in customers_obj:
        cinema_bar.sell_product(customer, customer.food)

    # make a movie session
    hall.movie_session(movie, customers_obj, cleaner_staff)

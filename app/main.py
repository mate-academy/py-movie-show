from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
):
    customers_list = []

    for people in customers:
        customer = Customer(people["name"], people["food"])
        cinema_bar = CinemaBar()

        cinema_bar.sell_product(customer, customer.food)

        customers_list.append(customer)

    cleaner_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    cinema_hall.movie_session(movie, customers_list, cleaner_staff)

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_list = []
    for person in customers:
        customer = Customer(person["name"], person["food"])
        customer_list.append(customer)
    cleaner_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for customer in customer_list:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customer_list, cleaner_staff)


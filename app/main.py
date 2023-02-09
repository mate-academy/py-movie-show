from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_list = [
        Customer(person["name"], person["food"]) for person in customers
    ]
    for customer in customer_list:
        CinemaBar().sell_product(customer.food, customer.name)
    hall = CinemaHall(hall_number)
    clean_staff = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, clean_staff)

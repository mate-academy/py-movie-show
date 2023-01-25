from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> str:
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))
    for people in customer_list:
        CinemaBar.sell_product(people, people.food)

    cinema_order = CinemaHall(hall_number)
    cleaning = Cleaner(cleaner)
    cinema_order.movie_session(movie, customer_list, cleaning)

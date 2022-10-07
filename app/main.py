from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_of_customers = []
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in customers:
        current_customer = Customer(customer["name"], customer["food"])
        list_of_customers.append(current_customer)
        CinemaBar.sell_product(customer=current_customer,
                               product=current_customer.food)
    cinema_hall.movie_session(movie, list_of_customers, cleaner)

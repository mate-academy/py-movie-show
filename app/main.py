from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)

    initialized_customers = []

    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        initialized_customers.append(customer)

    for customer in initialized_customers:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=initialized_customers,
        cleaning_staff=cleaner)

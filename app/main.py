from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_instances = []
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for i in range(len(customers)):
        name = customers[i]["name"]
        food = customers[i]["food"]
        customer = Customer(name, food)
        cinema_bar.sell_product(customer, food)
        customers_instances.append(customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_instances,
        cleaning_staff=cleaner)

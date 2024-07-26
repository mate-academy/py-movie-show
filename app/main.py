from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []
    for i in customers:
        customer = Customer(name=i["name"], food=i["food"])
        customer_instances.append(customer)

    bar_instance = CinemaBar()
    hall_instance = CinemaHall(hall_number)
    clean_instance = Cleaner(cleaner)

    for customer in customer_instances:
        bar_instance.sell_product(customer.food, customer)

    hall_instance.movie_session(movie, customer_instances, clean_instance)

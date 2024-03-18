from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_instances = []

    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        customers_instances.append(new_customer)

    hall_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()
    cleaner_instance = Cleaner(cleaner)

    for customer_instance in customers_instances:
        bar_instance.sell_product(product=customer_instance.food,
                                  customer=customer_instance)

    hall_instance.movie_session(movie_name=movie,
                                customers=customers_instances,
                                cleaning_staff=cleaner_instance)

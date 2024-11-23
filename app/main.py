from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    instances_customers_list = []
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        instances_customers_list.append(customer)
    hall_instance = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    for customer in instances_customers_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall_instance.movie_session(
        movie,
        instances_customers_list,
        cleaner_instance
    )

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
    customers_instances = []
    for customer_dict in customers:
        name = customer_dict.get("name")
        food = customer_dict.get("food")
        customer = Customer(name, food)
        customers_instances.append(customer)

    hall_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()
    cleaner_person = Cleaner(cleaner)

    for customer in customers_instances:
        bar_instance.sell_product(customer, customer.food)

    hall_instance.movie_session(movie, customers_instances, cleaner_person)

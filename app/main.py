from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str
                 ) -> None:
    customers_instances = []
    for customer_dict in customers:
        name = customer_dict.get("name")
        food = customer_dict.get("food")
        customer = Customer(name, food)
        customers_instances.append(customer)

    cinema_hall = CinemaHall(hall_number)
    bar_info = CinemaBar()
    cleaner_person = Cleaner(cleaning_staff)

    for customer in customers_instances:
        bar_info.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie_name, customers_instances, cleaner_person)

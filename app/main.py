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
    customers_instances_list = []
    cleaner_instance = Cleaner(cleaner)
    cinema_bar_instances = CinemaBar()
    hall = CinemaHall(hall_number)

    for person in customers:
        # making Customers instances
        customer = Customer(name=person["name"],
                            food=person["food"])
        customers_instances_list.append(customer)

    for person in customers_instances_list:
        # selling products
        cinema_bar_instances.sell_product(customer=person,
                                          product=person.food)

    hall.movie_session(
        movie_name=movie,
        customers=customers_instances_list,
        cleaning_staff=cleaner_instance
    )

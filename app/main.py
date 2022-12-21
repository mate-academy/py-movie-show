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
    customers_list = []
    cleaner_instance = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in customers:
        # making Customers instances
        customer = Customer(name=customer["name"], food=customer["food"])
        customers_list.append(customer)

        # selling food
        CinemaBar.sell_product(customer=customer.name, product=customer.food)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_instance
    )

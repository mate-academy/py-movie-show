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
    customer_instances = []
    cinema_bar = CinemaBar()
    for customer_iter in customers:
        name = customer_iter["name"]
        food = customer_iter["food"]
        customer = Customer(name=name, food=food)
        cinema_bar.sell_product(customer=customer, product=food)
        customer_instances.append(customer)

    cinema_hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )

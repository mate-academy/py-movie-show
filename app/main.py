from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_objects = []
    for customer in customers:
        customers_objects.append(
            Customer(name=customer["name"], food=customer["food"])
        )
    hall = CinemaHall(number=hall_number)
    cleaner_name = Cleaner(name=cleaner)
    for customer in customers_objects:
        CinemaBar.sell_product(
            customer=customer,
            product=customer.food
        )
    hall.movie_session(
        movie_name=movie,
        customers=customers_objects,
        cleaning_staff=cleaner_name
    )

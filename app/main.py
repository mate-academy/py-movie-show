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

    customer_instance = []
    for each_customer in customers:
        customer_instance.append(
            Customer(each_customer["name"],
                     each_customer["food"])
        )

    for each_customer in customer_instance:
        CinemaBar.sell_product(each_customer.food, each_customer)

    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=customer_instance,
        cleaning_staff=Cleaner(cleaner)
    )

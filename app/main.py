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
    hall_instance = CinemaHall(hall_number)
    bar_instance = CinemaBar()
    cleaner_instance = Cleaner(cleaner)
    customers_instances = []
    for customer in customers:
        customers_instances.append(
            Customer(name=customer["name"],
                     food=customer["food"])
        )
        bar_instance.sell_product(
            product=customers_instances[-1].food,
            customer=customers_instances[-1]
        )

    hall_instance.movie_session(
        movie_name=movie,
        customers=customers_instances,
        cleaning_staff=cleaner_instance
    )

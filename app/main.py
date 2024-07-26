from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie_name: str
) -> None:
    cb = CinemaBar()
    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(number=hall_number)

    for customers_info in customers:
        customer = Customer(
            name=customers_info["name"],
            food=customers_info["food"]
        )
        cb.sell_product(customer=customer, product=customers_info["food"])
    hall_instance.movie_session(
        movie_name=movie_name,
        customers=[Customer(name=c["name"], food=c["food"])
                   for c in customers],
        cleaning_staff=cleaner_instance
    )

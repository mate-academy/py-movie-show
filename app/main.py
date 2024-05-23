from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers_instance = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    for customer in customers_instance:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(
        movie_name=movie, customers=customers_instance, cleaning_staff=cleaner
    )

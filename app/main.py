from app.people.customer import Customer

from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaning_staff: str, movie_name: str) -> None:

    customers = [Customer(name=customer["name"], food=customer["food"]
                          )for customer in customers]

    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaning_staff)

    for customer in customers:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(movie_name=movie_name, customers=customers,
                              cleaning_staff=cleaner)

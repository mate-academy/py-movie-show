from app.cinema.bar import CinemaBar as seller
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    list_of_customers = []
    for customer_checker in customers:
        list_of_customers.append(
            Customer(name=customer_checker["name"],
                     food=customer_checker["food"])
        )

    for bar_work in list_of_customers:
        seller.sell_product(bar_work, bar_work.food)

    clean_stuf = Cleaner(name=cleaner)

    cinema = CinemaHall(number=hall_number)

    customers = list_of_customers

    CinemaHall.movie_session(cinema, movie, customers, clean_stuf)

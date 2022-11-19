from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customer_instance = [
        Customer(customer["name"],
                 customer["food"])
        for customer in customers]

    cinema_bar = CinemaBar()

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for each_customer in customer_instance:
        cinema_bar.sell_product(each_customer.food, each_customer)

    # 1) Do I need return cinema_hall.movie_session() or just do what I did?
    # 2) And if I wanted to return cinema_hall.movie_session(),
    # what I need return in annotation?
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instance,
        cleaning_staff=cleaning_staff)

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list | Customer,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_list = [
        Customer(customer["name"],
                 customer["food"]) for customer in customers]

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer_instance in customer_list:
        cinema_bar.sell_product(customer_instance.food, customer_instance)

    cinema_hall.movie_session(movie_name=movie, customers=customer_list,
                              cleaning_staff=cleaning_staff)

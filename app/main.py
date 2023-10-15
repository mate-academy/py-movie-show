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
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer_data in customers_list:
        CinemaBar.sell_product(customer_data, customer_data.food)
    hall.movie_session(movie, customers_list, cleaner)

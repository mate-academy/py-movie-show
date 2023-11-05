from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_instance_list = []
    for customer in customers:
        food = customer["food"]
        name = customer["name"]
        new_customer = Customer(name, food)
        customers_instance_list.append(new_customer)
        CinemaBar.sell_product(new_customer, food)

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customers_instance_list, cleaner)

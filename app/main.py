from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    for pupil in customers:
        customer_object = Customer(pupil["name"], pupil["food"])
        customers_list.append(customer_object)
        CinemaBar.sell_product(customer_object.food, customer_object)

    hall1 = CinemaHall(hall_number)
    cleaner1 = Cleaner(cleaner)
    hall1.movie_session(movie, customers_list, cleaner1)

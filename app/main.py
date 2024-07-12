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
    customers_list = [
        Customer(person["name"], person["food"])
        for person in customers
    ]
    cleaning_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()

    for person in customers_list:
        cinema_bar.sell_product(person.food, person)

    cinema_hall.movie_session(movie, customers_list, cleaning_staff)

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customers_lst = []
    for person in customers:
        customers_lst.append(Customer(person["name"], person["food"]))

    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for person in customers_lst:
        cinema_bar.sell_product(product=person.food, customer=person)

    hall.movie_session(
        movie_name=movie,
        customers=customers_lst,
        cleaning_staff=cleaner
    )

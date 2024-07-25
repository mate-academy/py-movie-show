from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        number: int,
        cleaner: str,
        movie: str
) -> None:
    ls = []
    cleaner_i = Cleaner(cleaner)
    hall = CinemaHall(number)
    for customer in customers:
        ls.append(Customer(customer["name"], customer["food"]))
    for customer in ls:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, ls, cleaner_i)

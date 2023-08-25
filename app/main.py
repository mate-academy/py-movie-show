from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,

                 cleaner: str, movie: str) -> None:
    hall1 = CinemaHall(hall_number)
    cleaner1 = Cleaner(cleaner)
    bar1 = CinemaBar()
    customers_resutl = []
    for i in customers:
        customers_resutl.append(Customer(i["name"], i["food"]))
    for i in customers_resutl:
        bar1.sell_product(i.food, i)
    hall1.movie_session(movie, customers_resutl, cleaner1)

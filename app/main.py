from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str
                 ) -> None:
    customers_nuw = [Customer(i["name"], i["food"]) for i in customers]
    for i in customers_nuw:
        CinemaBar.sell_product(i.food, i)
    cleaning_staff = Cleaner(cleaner)
    ch = CinemaHall(hall_number)
    ch.movie_session(movie_name=movie,
                     customers=customers_nuw,
                     cleaning_staff=cleaning_staff
                     )

from app.people import cinema_staff
from app.people import customer
from app.cinema import bar
from app.cinema import hall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    cb = bar.CinemaBar
    ch = hall.CinemaHall(hall_number)
    list_customer = [customer.Customer(custom["name"], custom["food"])
                     for custom in customers]
    clean = cinema_staff.Cleaner(cleaner)
    for value in list_customer:
        cb.sell_product(value.name, value.food)
    ch.movie_session(movie, list_customer, clean)

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
    guests = [Customer(customer["name"], customer["food"])
              for customer in customers]
    hall_num = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    cinema_bar = CinemaBar
    for guest in guests:
        cinema_bar.sell_product(guest, guest.food)
    hall_num.movie_session(movie, guests, cleaner_name)

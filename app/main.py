from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    client = []
    for customer in customers:
        client.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    bar_cinema = CinemaBar()
    staff = Cleaner(cleaner)

    for customer in client:
        bar_cinema.sell_product(customer.food, customer)
    hall.movie_session(movie, client, staff)

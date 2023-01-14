from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    hall = CinemaHall(number=hall_number)
    watchers = []
    for watcher in customers:
        customer = Customer(name=watcher["name"], food=watcher["food"])
        watchers.append(customer)
    for user in watchers:
        CinemaBar.sell_product(user.food, user)
    staff_member = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie, customers=watchers, cleaning_staff=staff_member
    )

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    object_cinema_hall = CinemaHall(hall_number)
    object_cleaner = Cleaner(cleaner)
    object_customer = []
    for man in customers:
        object_customer.append(Customer(man["name"], man["food"]))
    for obj in object_customer:
        CinemaBar.sell_product(obj, obj.food)

    object_cinema_hall.movie_session(movie, object_customer, object_cleaner)


# customers = [
#     {"name": "Bob", "food": "Coca-cola"},
#     {"name": "Alex", "food": "popcorn"}
# ]
# hall_number = 5
# cleaner_name = "Anna"
# movie = "Madagascar"
# cinema_visit(customers=customers,
#              hall_number=5,
#              cleaner="Anna",
#              movie="Madagascar")

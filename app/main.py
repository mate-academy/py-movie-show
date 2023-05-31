from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    instances_of_customers = []
    for person in customers:
        new_customer = Customer(person["name"], person["food"])
        instances_of_customers.append(new_customer)
    for person in instances_of_customers:
        cinema_bar.sell_product(person, person.food)
    cinema_hall.movie_session(movie, instances_of_customers, cinema_cleaner)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(
    customers=customers,
    hall_number=5,
    cleaner="Anna",
    movie="Madagascar"
)

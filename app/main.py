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
    customers_list = []

    for customer in customers:
        # making Customers instances
        customer = Customer(name=customer["name"], food=customer["food"])
        customers_list.append(customer)

        # selling food
        CinemaBar.sell_product(customer=customer.name, product=customer.food)

    cleaner_instance = Cleaner(cleaner)

    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_instance
    )


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
# Cinema bar sold Coca-cola to Bob.
# Cinema bar sold popcorn to Alex.
# "Madagascar" started in hall number 5.
# Bob is watching "Madagascar".
# Alex is watching "Madagascar".
# "Madagascar" ended.
# Cleaner Anna is cleaning hall number 5.

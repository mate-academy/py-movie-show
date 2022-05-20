from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_obj = []
    for i in customers:
        customers_obj.append(Customer(i["name"], i["food"]))

    for customer in customers_obj:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    clean = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, customers_obj, clean)

    clean.clean_hall(hall_number)


customers_ = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number_ = 5
cleaner_name_ = "Anna"
movie_ = "Madagascar"
cinema_visit(customers=customers_, hall_number=4, cleaner="John", movie="Madagascar")

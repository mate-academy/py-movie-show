from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_instance, customer["food"])

    cleaning = Cleaner(name=cleaner)
    cinema_instance = CinemaHall(hall_number)
    customer_instance = []
    for customer in customers:
        customer_instance.append(Customer(customer["name"], customer["food"]))

    CinemaHall.movie_session(cinema_instance, movie, customer_instance,
                             cleaning)


if __name__ == '__main__':
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=5, cleaner="Anna",
                       movie="Madagascar")
    # Cinema bar sold Coca-cola to Bob.
    # Cinema bar sold popcorn to Alex.
    # "Madagascar" started in hall number 5.
    # Bob is watching "Madagascar".
    # Alex is watching "Madagascar".
    # "Madagascar" ended.
    # Cleaner Anna is cleaning hall number 5.

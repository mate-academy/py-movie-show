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
    customers_instances = [
        Customer(**customer)
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_instance = Cleaner(cleaner)

    for customer in customers_instances:
        cinema_bar.sell_product(
            customer.food,
            customer
        )
    cinema_hall.movie_session(
        movie,
        customers_instances,
        cleaner_instance
    )


if __name__ == "__main__":
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

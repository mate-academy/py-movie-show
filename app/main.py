from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner_name: str, movie: str) -> None:
    for i in customers:
        customer = Customer(i["name"], i["food"])
        CinemaBar.sell_product(customer, customer.food)

    cleaner = Cleaner(cleaner_name)

    cinema_hall = CinemaHall(hall_number)

    (cinema_hall.movie_session
     (movie, [Customer(i["name"], i["food"]) for i in customers], cleaner))


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=hall_number,
                 cleaner_name=cleaner_name, movie=movie)

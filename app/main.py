# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    # write you code here
    customers_arr = []
    for custom in customers:
        customers_arr.append(Customer(custom["name"], custom["food"]))
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_name = Cleaner(cleaner)
    for custom in customers_arr:
        cinema_bar.sell_product(custom, custom.food)
    cinema_hall.movie_session(movie, customers_arr, cleaner_name)


if __name__ == '__main__':
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=5,
                 cleaner="Anna", movie="Madagascar")

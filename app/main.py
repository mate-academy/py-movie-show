from cinema.hall import CinemaHall
from people.cinema_staff import Cleaner
from people.customer import Customer
from cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)
    bar = CinemaBar()

    customers_obj = []

    for raw_customer in customers:
        customers_obj.append(Customer(raw_customer['name'], raw_customer['food']))
    for customer in customers_obj:
        bar.sell_product(customer.food, customer)

    hall.movie_cinema(movie, customers_obj, current_cleaner)


if __name__ == '__main__':
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")
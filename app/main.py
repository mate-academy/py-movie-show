from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers_info: list,
                 hall_number: int,
                 cleaner_name: str,
                 movie_name: str) -> callable:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    # Створення екземплярів клієнтів зі списку словників customers_info
    customer_instances = [Customer(info['name'], info['food'])
                          for info in customers_info]

    # Продаж продуктів клієнтам у кінобарі
    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)

    # Проведення кіносеансу в кінозалі
    cinema_hall.movie_session(movie_name, customer, cleaner)

    # Прибирання залу після кіносеансу
    cleaner.clean_hall(hall_number)

customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")
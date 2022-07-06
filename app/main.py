from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cust_name_food = [Customer(cust["name"], cust["food"]) for cust in customers]
    cleaner = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)
    for customer in cust_name_food:
        customer = Customer(customer.name, customer.food)
        CinemaBar.sell_product(customer.food, customer.name)
    CinemaHall.movie_session(hall_number, movie, customers, cleaner)



















# В модуле main.py вы должны импортировать все эти классы. Классы следует импортировать по абсолютному пути,
# который начинается с «app». с ключевым словом «from». Напишите функцию cinema_visit,
# которая принимает movie_name, customers- список клиентов, элементы - слова с именем и желаемой "едой" клиента,
# cleaning_staff- имя уборщицы, которая будет убирать зал после киносеанса.
# Эта функция должна создавать Customers экземпляры, экземпляры CinemaHall и CinemaBar, экземпляры Cleaner.
# Сначала кинобар должен продавать посетителям еду, затем кинозал должен проводить киносеанс и, наконец, уборщица убирает кинозал.
# customers = [
#                      {"name": "Susan", "food": "Pepsi"},
#                      {"name": "Michael", "food": "Coca-cola"},
#                      {"name": "Monica", "food": "popcorn"}
#                  ]
# print(cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar"))
# Пример:
#
# customers = [{"name": "Bob", "food": "Coca-cola"}, {"name": "Alex", "food": "popcorn"}]
# hall_number = 5
# cleaner_name = "Anna"
# movie = "Madagascar"
# print(cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar"))
# # Cinema bar sold Coca-cola to Bob.
# # Cinema bar sold popcorn to Alex.
# # "Madagascar" started in hall number 5.
# # Bob is watching "Madagascar".
# # Alex is watching "Madagascar".
# # "Madagascar" ended.
# # Cleaner Anna is cleaning hall number 5.
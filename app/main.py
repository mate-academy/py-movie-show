from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    for i in customers:
        customer = Customer(i.get("name"), i.get("food"))
        customers_list.append(customer)
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall = CinemaHall(hall_number)
    cleaning_person = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_list, cleaning_person)

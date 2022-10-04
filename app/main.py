# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # write you code here
    customers_list = []
    for customer_dict_elements in customers:
        customer = Customer(customer_dict_elements["name"],
                             customer_dict_elements["food"])
        customers_list.append(customer)
    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)
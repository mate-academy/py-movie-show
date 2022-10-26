from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_list = []
    for customer in customers:
        customer_list.append(Customer(customer["name"], customer["food"]))

    for person in customer_list:
        CinemaBar.sell_product(person.food, person)

    # CinemaBar.sell_product(customer_list)
    CinemaHall(hall_number)
    Cleaner(cleaner)
    CinemaHall.movie_session(movie, customer_list, cleaner)








    CinemaBar.sell_product(customer_list)
    new_hall_number = CinemaHall(hall_number)
    new_cleaner = Cleaner(cleaner)
    new_hall_number.movie_session(movie, customers, new_cleaner)

    
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_of_customers = []
    cinema_hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    for person in customers:
        customer_member = Customer(person['name'], person['food'])
        cinema_bar.sell_product(customer_member.food, customer_member)
        list_of_customers.append(customer_member)
    cinema_hall.movie_session(movie, list_of_customers, staff)

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_customers = []
    for people in customers:
        cinema_bar = CinemaBar()
        customer = Customer(people["name"], people["food"])
        cinema_bar.sell_product(customer, customer.food)
        list_customers.append(customer)

    cleaner_person = Cleaner(name=cleaner)
    clean_hall = CinemaHall(number=hall_number)
    clean_hall.movie_session(movie_name=movie,
                             customers=list_customers,
                             cleaning_staff=cleaner_person
                             )

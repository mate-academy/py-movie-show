from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers, hall_number, cleaner, movie):
    clients = []
    for viewer in customers:
        cinema_bar = CinemaBar()
        customer = Customer(viewer["name"], viewer["food"])
        cinema_bar.sell_product(customer, customer.food)
        clients.append(customer)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie,
                       customers=clients,
                       cleaning_staff=Cleaner(name=cleaner))

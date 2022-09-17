from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for index in range(len(customers)):
        customers[index] = Customer(customers[index]["name"]
                                    , customers[index]["food"])
    for person in customers:
        CinemaBar.sell_product(person.food, person)
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    hall.movie_session(movie, customers, staff)

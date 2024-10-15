from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    movie_customers = [Customer(name=customer["name"], food=customer["food"]) for customer in customers]
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner_staff = Cleaner(name=cleaner)

    for customer in movie_customers:
        cinema_bar.sell_product(product=customer.food, customer=customer)
    cinema_hall.movie_session(movie, movie_customers, cleaner_staff)

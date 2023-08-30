from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

def cinema_visit(customers, hall_number, cleaner, movie):
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer_data in customers:
        customer = Customer(name=customer_data["name"], food=customer_data["food"])
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=[Customer(**i) for i in customers],
        cleaning_staff=Cleaner(name=cleaner)
    )
    
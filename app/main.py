from people.customer import Customer
from people.cinema_staff import Cleaner
from cinema.bar import CinemaBar
from cinema.hall import CinemaHall

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_of_customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
        ]
    cinema_hall = CinemaHall(hall_number=hall_number)
    cleaner_work = Cleaner(name=cleaner)

    for customer in customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    cinema_hall.movie_session(movie_name=movie, customers=list_of_customers, cleaning_staff=cleaner_work)

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: Cleaner | str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer_data in customers:
        customer = Customer(name=customer_data["name"], food=customer_data["food"])
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall.movie_session(movie, [Customer(**c) for c in customers], cleaner)


customers_t = [{'food': 'Coca-cola', 'name': 'Bob'},
             {'food': 'popcorn', 'name': 'Alex'}]
hall_number_t = 5
cleaner_t = 'Anna'
movie_t = 'Madagascar'
cinema_visit(customers_t, hall_number_t, cleaner_t, movie_t)

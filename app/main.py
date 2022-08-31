from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    bar = CinemaBar()
    cleaning_staff = Cleaner(cleaner)
    for cust in customers:
        
        customer = Customer(cust['name'], cust['food'])
        bar.sell_product(cust['name'], customer)
        
        cd = customer.watch_movie(movie)
        n_hall = CinemaHall(hall_number)
        n_hall.movie_session(movie, cd, cleaning_staff)
    cleaning_staff.clean_hall(hall_number)










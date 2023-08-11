from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner

def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str):
    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(cleaner_name)

    customer_list = []
    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data.get("food"))
        customer_list.append(customer)
        if customer.food is not None:
            CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie_name = movie_name,
                              customers = customers_list,
                              cleaning_staff = cleaner)
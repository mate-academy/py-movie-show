from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    list_customers = []
    for i in customers:
        list_customers.append(Customer(i["name"], i["food"]))
    for customer in range(len(list_customers)):
        new_customer = CinemaBar()
        new_customer.sell_product(customers[customer]["food"],
                                  list_customers[customer]
                                  )
    cinema = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    cinema.movie_session(movie, list_customers, staff)

# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cus_ins_ls = []
    cinema_session = CinemaHall(hall_number)
    staff = Cleaner(cleaner)

    for customer in customers:
        cus_ins_ls.append(Customer(customer.get("name"), customer.get("food")))

    for customer in cus_ins_ls:
        CinemaBar.sell_product(customer.food, customer)

    cinema_session.movie_session(movie, cus_ins_ls, staff)

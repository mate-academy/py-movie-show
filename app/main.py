from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: [Customer],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    # better to use keyword arg in Customer?
    # whether to use them if dict val. were different?
    # not like Customer args (name - dict['name'])?
    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in customers_list:
        CinemaBar().sell_product(customer.food, customer)
    CinemaHall(hall_number).movie_session(
        movie_name,
        customers_list,
        Cleaner(cleaning_staff)
    )
    # Cleaner(cleaning_staff).clean_hall(hall_number)  # Comment only for me

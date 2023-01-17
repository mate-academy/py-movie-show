from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    for person in customers:
        customers_list.append(Customer(
            name=person["name"],
            food=person["food"]
        ))

    bar_of_cinema = CinemaBar()
    for customer in customers_list:
        bar_of_cinema.sell_product(product=customer.food, customer=customer)

    clean_staff = Cleaner(name=cleaner)
    new_hall = CinemaHall(number=hall_number)
    new_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=clean_staff
    )

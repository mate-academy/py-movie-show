from app.cinema import bar
from app.cinema import hall
from app.people import customer
from app.people import cinema_staff


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = [customer.Customer(client["name"], client["food"]) for client in customers.items()]
    cinema_hall = hall.CinemaHall(hall_number)
    cleaner_staff = cinema_staff.Cleaner(cleaner)
    cinema_bar = bar.CinemaBar()

    for client in customers_list:
        cinema_bar.sell_product(client.food, client)

    cinema_hall.movie_session(movie, customers_list)
    cleaner_staff.clean_hall(hall_number)

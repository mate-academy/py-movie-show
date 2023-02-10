from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner_name: str, movie: str):
    for customer_data in customers:
        customer_name = customer_data["name"]
        food = customer_data["food"]
        print(f"Cinema bar sold {food} to {customer_name}.")

    cleaner = Cleaner(cleaner_name)
    cinema_hall = CinemaHall(hall_number, cleaner)

    movie_session = cinema_hall.movie_session1(movie)

    for customer_data in customers:
        customer_name = customer_data["name"]
        customer = Customer(customer_name, food)
        customer.watch_movie(movie)

    movie_session = cinema_hall.movie_session(movie)

    print(f"Cleaner {cleaner_name} is cleaning hall number {hall_number}.")


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5, cleaner_name=cleaner_name, movie=movie)

from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    arr_customers = []
    for customer in customers:
        arr_customers.append(Customer(customer["name"], customer["food"]))
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in arr_customers:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(movie_name=movie, customers=arr_customers,
                              cleaning_staff=cleaner
                              )


if __name__ == '__main__':
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=5,
                 cleaner="Anna", movie="Madagascar")

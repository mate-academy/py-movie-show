from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(movie_name, customers, hall_number, cleaning_staff):
    # Create instances of CinemaBar, CinemaHall, and Cleaner
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaning_staff)
    
    # Sell food to customers at the cinema bar
    for customer_info in customers:
        customer = Customer(name=customer_info['name'], food=customer_info['food'])
        cinema_bar.sell_product(product=customer_info['food'], customer=customer)
    
    # Start movie session in the cinema hall
    cinema_hall.movie_session(movie_name=movie_name, customers=[Customer(name=customer_info['name'], food=customer_info['food']) for customer_info in customers], cleaning_staff=cleaner)

# Example usage:
customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(movie_name=movie, customers=customers, hall_number=hall_number, cleaning_staff=cleaner_name)

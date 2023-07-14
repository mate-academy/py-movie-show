from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    try:
        for customer in customers:
            CinemaBar.sell_product(customer=Customer(customer.get("name"),
                                                     customer.get("food")),
                                   product=customer.get("food"))
    except:
        CinemaBar.sell_product(customer=Customer(customer.name,
                                                 customer.food),
                               product=customer.food)
    cinema_hall_instance = CinemaHall(hall_number)
    cinema_hall_instance.movie_session(cleaning_staff=cleaner,
                                       customers=customers,
                                       movie_name=movie)
    cleaner = Cleaner(cleaner)
    cleaner.clean_hall(hall_number)

customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")

#t[customers1-5-Anna-Madagascar-Cinema bar sold Coca-cola to Bob.\nCinema bar sold popcorn to Alex.\n"Madagascar" started in hall number 5.\nBob is watching "Madagascar".\nAlex is watching "Madagascar".\n"Madagascar" ended.\nCleaner Anna is cleaning hall number 5.\n]

# write your imports here


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    for customer_data in customers:
        custoner = Customer(name=customer_data["name"], food=customer_data["food"])
        cinema_bar.sell_product(customer. customer.food)

    cinema_hall.mavie_sessions(
        movie_name,
        [Customer(name=customer_data["name"], food=customer_data["food"]) for customer_data in customers],
        cleaner
    )

customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")

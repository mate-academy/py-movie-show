from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list, cleaning_stuff=Cleaner) -> None:
        print(f"'{movie_name}' start")
        if customers != []:
            for one_customer in customers:
                client = Customer(name=one_customer.get("name"), food=one_customer.get("food"))
                client.watch_movie(movie_name)
        print(f"'{movie_name}' end")
        cleaner = Cleaner(cleaning_stuff)
        cleaner.clean_hall(self.number)

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list[Customer],
                      cleaning_staff: str) -> None:
        print(f""""{movie_name}" started in hall number {self.number}.""")
        for person in customers:
            if isinstance(person, Customer):
                Customer(person.name, person.food).watch_movie(movie_name)
            else:
                Customer(person["name"],
                         person["food"]).watch_movie(movie_name)
        print(f""""{movie_name}" ended.""")
        Cleaner.clean_hall(cleaning_staff, self.number)

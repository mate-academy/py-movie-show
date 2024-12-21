from app.people.customers import watch_movie
from app.people.cinema_staff import clean_hall


class CinemaHall:
    def __init__(self, number):
        self.number = number
    
    def movie_session(self, movie_name: str, customers: list, cleaning_staff):
        print(f"Movie {movie_name} starts in hall {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie {movie_name} ends!")
        for st_mem in cleaning_staff:
            st_mem.clean_hall(self.number)

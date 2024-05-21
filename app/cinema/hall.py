class CinemaHall:
    def __init__(self, number: str):
        self.number = number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff):
        watch_movie(movie_name, customers, cleaning_staff)
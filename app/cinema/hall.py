class CinemaHall:
    def __init__(self, number_halls):
        self.number_halls = number_halls

    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f'"{movie_name}" started in hall number {self.number_halls}."')
        for person in customers:
            person.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number_halls)

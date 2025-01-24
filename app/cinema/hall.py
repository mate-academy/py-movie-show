from app.cinema.cinema_staff import Cleaner
class CinemaHall:

    def __init__(self, number: int):
        self.number = number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff: Cleaner ):
        print (f"{movie_name} started in hall number {self.number}.")
        for person in customers:
            print ( f"{person["name"]} is watching {movie_name}.")
        print(f"{movie_name} ended.")
        cleaning_staff.clean_hall(hall_number = self.number)

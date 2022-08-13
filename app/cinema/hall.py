from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f"\"{movie_name}\" started in hall number {self.number}.")
        for elems in customers:
            Customer.watch_movie(elems, movie_name)
        print(f"\"{movie_name}\" ended.\n"
              f"Cleaner {cleaning_staff.name} is cleaning"
              f" hall number {self.number}.")

# from app.people.cinema_staff import Cleaner
# from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int):
        self.number = number

    def movie_session(self, movie_name: str, customers: list,
                      cleaning_staff):
        print(f'"{movie_name}" started in hall number {self.number}.')
        for i in range(len(customers)):
            customers[i].watch_movie(movie_name)
            i += 1

        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)


if __name__ == '__main__':
    number = 5
    ch = CinemaHall(number)
    movie_name = "Madagascar"

    customers = [Customer(name="Bob", food="popcorn"),
                 Customer(name="Robbert", food="cola")]
    cleaning_staff = Cleaner(name="Anna")
    ch.movie_session(movie_name=movie_name, customers=customers,
                     cleaning_staff=cleaning_staff)

    # "Madagascar" started in hall number 5.
    # Bob is watching "Madagascar".
    # Alex is watching "Madagascar".
    # "Madagascar" ended.
    # Cleaner Anna is cleaning hall number 5.

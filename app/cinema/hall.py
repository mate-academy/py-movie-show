class CinemaHall:
    def __init__(self, hall_num):
        self.hall_num = hall_num
    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f"{movie_name} starts at {self.hall_num} !")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"{movie_name} at {self.hall_num} ended")
        cleaning_staff.clean_hall(self.hall_num)

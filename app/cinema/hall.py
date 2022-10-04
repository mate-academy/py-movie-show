class CinemaHall:

    def __init__(self, number):
        self.number = number

    def movie_session(self, movie_name, 
                      customers: list, 
                      cleaning_staff):
        print("Movie start")
        watch_movie()
        print("Movie end")
        clean_hall()
class CinemaHall:
    def __init_(self, number):
        self.number = number
    
    def movie_session(movie_name: str, customers: list, cleaning_staff, hall_number):
        print(f"Movie {movie_name} starts.")
        for customer in customers:
            watch_movie(movie_name, customer)
        print(f"Movie {movie_name} ends!")
        for st_mem in cleaning_staff:
            clean_hall(st_mem, hall_number)

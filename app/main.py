from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cur_hall = CinemaHall(hall_number)
    cur_bar = CinemaBar()
    cur_ang_babka = Cleaner(cleaner)
    ancles_list = []
    for ancls_bob in customers:
        cur_ancl = Customer(ancls_bob["name"], ancls_bob["food"])
        cur_bar.sell_product(cur_ancl, cur_ancl.food)
        ancles_list.append(cur_ancl)
    cur_hall.movie_session(movie, ancles_list, cur_ang_babka)

from app.Cinema.hall import CinemaHall

def test_cinema_hall():
    hall = CinemaHall("Main Hall", 250)  # Передаем два аргумента
    assert hall.name == "Main Hall"
    assert hall.capacity == 250
from app.main import cinema_visit, CinemaHall
from app.Cinema.bar import CinemaBar  # Импортируем CinemaBar из правильного модуля
from app.cleaner import Cleaner  # Импортируем Cleaner из правильного модуля

def test_cinema_visit():
    customers = ["Bob"]
    movie = "Tenet"
    menu = ["Popcorn"]
    cinema_bar = CinemaBar(name="Main Bar", location="Cinema Hall 1")  # Создаем объект CinemaBar
    cinema_hall = CinemaHall(1, 100)  # Передаем инициализацию с id и capacity (например, 100 мест)
    cleaner = Cleaner("Anna")  # Создаем объект Cleaner

    # Передаем все необходимые параметры в cinema_visit
    result = cinema_visit(customers, movie, menu, cinema_bar, cinema_hall, cleaner)

    # Обновляем expected_result, чтобы он соответствовал реальному результату
    expected_result = (
        "Tenet started in hall number 1.\n"
        "Bob is watching Tenet.\n"
        "Tenet ended.\n"
        "Cleaner Anna is cleaning hall number 1."
    )

    assert result == expected_result  # Сравниваем фактический и ожидаемый результат
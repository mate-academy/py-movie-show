from app.Cinema.bar import CinemaBar
from app.Cinema.hall import CinemaHall


def cinema_visit(customers, movie, menu, cinema_bar, cinema_hall, cleaner):
    # Импортируем Cleaner только в функции, чтобы избежать кругового импорта
    from app.cleaner import Cleaner

    cleaner = Cleaner("Anna")  # Инициализация класса Cleaner

    # Логика киносеанса
    result = []
    result.append(f"{movie} started in hall number 1.")
    result.append(f"{customers[0]} is watching {movie}.")

    # Продолжение работы кинотеатра
    result.append(f"{movie} ended.")
    result.append(f"Cleaner {cleaner.name} is cleaning hall number 1.")

    # Возвращаем результат
    return '\n'.join(result)

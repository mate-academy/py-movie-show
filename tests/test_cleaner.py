from app.cleaner import Cleaner

def test_cleaner_clean_hall():
    cleaner = Cleaner("Anatoly")
    result = cleaner.clean_hall(9)  # Используем метод clean_hall
    assert result == "Cleaner Anatoly is cleaning hall number 9."

class Cleaner:

    def __init__(self, name):
        self.name = name

    def clean_hall(self, hall_number):
        print(f'Cleaner {self.name} is cleaning hall number {hall_number}.')










# cinema_staff- внутри этого модуля создается Cleaner класс,
# его конструктор берет и сохраняет name.
# Этот класс должен иметь только один метод clean_hall,
# этот метод принимает hall_number номер зала,
# который должен убрать уборщик, и выводит, что уборщик убирает этот зал.
# anna = Cleaner(name="Anna")
# anna.clean_hall(hall_number=5)
# # Cleaner Anna is cleaning hall number 5.
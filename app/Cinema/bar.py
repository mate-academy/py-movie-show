class CinemaBar:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def sell_food(self, customer, food_item, menu):
        if food_item in menu:
            print(f"{customer['name']} bought {food_item} from {self.name}!")
        else:
            print(f"Sorry, {food_item} is not available in the menu.")
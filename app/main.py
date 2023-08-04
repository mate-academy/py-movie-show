from cinema import bar
from cinema import hall
from people import cinema_staff
from people import customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    # Create instances
    cinema_hall = hall.CinemaHall(hall_number)
    cinema_bar = bar.CinemaBar()
    cleaner_instance = cinema_staff.Cleaner(cleaner)

    # Create customer instances
    customer_instances = [
        customer.Customer(cust["name"],
                          cust["food"]
                          ) for cust in customers]

    # Sell food in the bar
    for cust_instance in customer_instances:
        cinema_bar.sell_product(
            cust_instance.name,
            cust_instance.food)

    cinema_hall.movie_session(
        movie,
        customer_instances,
        cleaner_instance)

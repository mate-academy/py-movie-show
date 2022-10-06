from app.people.customer import Customer

class CinemaBar:
    
    @staticmethod
    def sell_product(product: str, customer: Customer):
        print(f"CinemaBar sold {product} to {customer.name}")

from chatbot_base import ChatbotBase

class Coffee:
    def __init__(self, size=None, milk_type=None):
        self.size = size
        self.milk_type = milk_type
        self.with_milk = milk_type is not None
        self.base_price = 0  

    def get_price(self):
        return self.base_price

    def to_str(self):
        return f"A {self.size} coffee"

    def to_dict(self):
        return {
            'drink': self.__class__.__name__.lower(),
            'size': self.size,
            'with_milk': self.with_milk,
            'milk_type': self.milk_type,
            'price': self.get_price()
        }

class Cappuccino(Coffee):
    def __init__(self, size, milk_type):
        super().__init__(size, milk_type)
        self.base_price = 350

    def get_price(self):
        if self.milk_type in ["whole", "skimmed"]:
            milk_price = 0
        elif self.milk_type in ["oat", "soya"]:
            milk_price = 20
        elif self.milk_type == "almond":
            milk_price = 50

        size_price = {"small": 0, "medium": 50, "large": 90}.get(self.size, 0)

        return self.base_price + milk_price + size_price

    def to_str(self):
        return f"A {self.size} cappuccino with {self.milk_type} milk" if self.with_milk else f"A {self.size} cappuccino"


class Americano(Coffee):
    def __init__(self, size, milk_type=None):
        super().__init__(size, milk_type)
        self.base_price = 220  

    def get_price(self):
        if self.milk_type in ["whole", "skimmed"]:
            milk_price = 0
        elif self.milk_type in ["oat", "soya"]:
            milk_price = 20
        elif self.milk_type == "almond":
            milk_price = 50

        size_price = {"small": 0, "medium": 50, "large": 90}.get(self.size, 0)
        return self.base_price + milk_price + size_price

    def to_str(self):
        if self.with_milk:
            return f"A {self.size} white americano with {self.milk_type} milk"
        else:
            return f"A {self.size} black americano"

class FlatWhite(Coffee):
    def __init__(self, milk_type):
        super().__init__(size="small", milk_type=milk_type) 
        self.base_price = 250 

    def get_price(self):
        if self.milk_type in ["whole", "skimmed"]:
            milk_price = 0
        elif self.milk_type in ["oat", "soya"]:
            milk_price = 20
        elif self.milk_type == "almond":
            milk_price = 50

        return self.base_price + milk_price

    def to_str(self):
        return f"A flat white with {self.milk_type} milk" if self.with_milk else "A flat white"

class Espresso(Coffee):
    def __init__(self, size, milk_type=None):
        super().__init__(size, milk_type)
        self.base_price = 180

    def get_price(self):
        size_price = {"double": 20, "single": 50}.get(self.size, 0) 
        return self.base_price + size_price

    def to_str(self):
        return f"A {self.size} espresso"


def take_order():
    print("Welcome to the Coffee Shop!")
    orders = []
    
    while True:
        drink_type = input("What would you like to drink? (cappuccino, americano, flat white, espresso)\n").strip().lower()
        
        if drink_type == "cappuccino":
            size = input("What size? (small, medium, large)\n").strip().lower()
            milk_type = input("What type of milk? (whole, skimmed, oat, soya, almond)\n").strip().lower()
            order = Cappuccino(size, milk_type)

        elif drink_type == "americano":
            size = input("What size? (small, medium, large)\n").strip().lower()
            milk_type = input("What type of milk? (whole, skimmed, oat, soya, almond, or none)\n").strip().lower() or None
            order = Americano(size, milk_type)
        
        elif drink_type == "flat white":
            milk_type = input("What type of milk? (whole, skimmed, oat, soya, almond)\n").strip().lower()
            order = FlatWhite(milk_type)
        
        elif drink_type == "espresso":
            size = input("What size? (single, double)\n").strip().lower()
            order = Espresso(size)
        
        else:
            print("I did not understand.")
            continue

        orders.append(order)
        more_orders = input("Would you like to order another drink? (yes/no)\n").strip().lower()
        if more_orders != "yes":
            break

    print("\nYour orders:")
    total_price = 0
    for order in orders:
        print(order.to_str())
        total_price += order.get_price()

    print(f"\nTotal price: £{total_price / 100:.2f}")

def take_order():
    print("Welcome to the Coffee Shop!")
    orders = []
    
    while True:
        drink_type = input("What would you like to drink? (cappuccino, americano, flat white, espresso)\n").strip().lower()
        
        if drink_type == "cappuccino":
            size = input("What size? (small, medium, large)\n").strip().lower()
            milk_type = input("What type of milk? (whole, skimmed, oat, soya, almond)\n").strip().lower()
            order = Cappuccino(size, milk_type)

        elif drink_type == "americano":
            size = input("What size? (small, medium, large)\n").strip().lower()
            milk_type = input("What type of milk? (whole, skimmed, oat, soya, almond, or none)\n").strip().lower() or None
            order = Americano(size, milk_type)
        
        elif drink_type == "flat white":
            milk_type = input("What type of milk? (whole, skimmed, oat, soya, almond)\n").strip().lower()
            order = FlatWhite(milk_type)
        
        elif drink_type == "espresso":
            size = input("What size? (single, double)\n").strip().lower()
            order = Espresso(size)
        
        else:
            print("I did not understand.")
            continue

        orders.append(order)
        more_orders = input("Would you like to order another drink? (yes/no)\n").strip().lower()
        if more_orders != "yes":
            break
    
    customer_name = input("May I have your name, please?\n").strip()
    print(f"\nThank you, {customer_name}! Here is your order:")
    total_price = 0
    for order in orders:
        print(order.to_str())
        total_price += order.get_price()

    print(f"\nTotal price: £{total_price / 100:.2f}")
    print(f"Have a great day, {customer_name}!")

take_order()



#随便的更改

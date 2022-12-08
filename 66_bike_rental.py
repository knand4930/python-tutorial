"""
example

1. Display Available bikes
2. Request a bike for rent(100Rs -> 1qty)
3. Exit
"""


class BikeShop:
    def __init__(self, stock):
        self.stock = stock

    def displayBike(self):
        print("Total Bikes ", self.stock)

    def rentBike(self, q):
        if q <= 0:
            print("Enter the Positive value or greater than Zero")
        elif q >= self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock = self.stock - q
            print("Total Price ", q * 100)
            print("Total Stock ", self.stock)

while True:
    obj = BikeShop(100)
    uc = int(input("""
    1. Display Stock
    2. Rent a Bike
    3. Exit
    """))

    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        n = int(input("Enter the Quantity : "))
        obj.rentBike(n)
    else:
        break
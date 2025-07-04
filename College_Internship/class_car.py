class car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def dispaly_details(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Price: ", self.price)
        print("----------------------------------")

brand1 = input("Enter the brand of the car: ")
model1 = input("Enter the model of the car: ")
price1 = float(input("Enter the price of the car: "))

car1 = car(brand1, model1, price1)

car2 = car("Toyota", "Camry", 3000000.0)

print("\nCar 1 Details:")
car1.dispaly_details()
car2.dispaly_details()
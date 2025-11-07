class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def drive(self):
        print("Akash is driving the car")
    
    def stop_the_car(self):
        print("Akash stopped the car")
    
    def __str__(self):
        return f"Car: {self.name} {self.model} in {self.color} color"
    
    def display_info(self):
        print(f"Car Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
    

my_car = Car("Audi", "e-tron GT", "Silver")

# Method 1: Print individual attributes
print("Car Name:", my_car.name)
print("Model:", my_car.model)
print("Color:", my_car.color)

print("\n" + "="*30 + "\n")

# Method 2: Use the display_info method
my_car.display_info()

print("\n" + "="*30 + "\n")

# Method 3: Print the whole object (using __str__ method)
print(my_car)

print("\n" + "="*30 + "\n")

# Method 4: Using f-string
print(f"My car is a {my_car.color} {my_car.name} {my_car.model}")

print("\n" + "="*30 + "\n")

my_car.drive()
my_car.stop_the_car()



def get_car():
    yield "Car 1"
    yield "Car 2"
    yield "Car 3"
    
cars = get_car()
print(next(cars))
print(next(cars))
print(next(cars))

# Because the above print statements consume all values from the generator,
# the generator is exhausted, so the for loop has nothing left to iterate over.

for car in cars:
    print("-",car) 
    

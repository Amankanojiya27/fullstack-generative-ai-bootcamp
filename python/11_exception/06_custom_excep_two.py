class OutOfIngredientError(Exception):
    pass

def make_chai(milk,suger):
    if milk == 0 or suger == 0:
        raise OutOfIngredientError("Missing Milk or suger")
    print("chai is ready")
    
make_chai(5,1)
print()
make_chai(0,1)

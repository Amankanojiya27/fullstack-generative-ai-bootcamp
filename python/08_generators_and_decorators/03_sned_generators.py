# Send Value to Generators

def chai_custmor():
    print("Welcome to chai shop !")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_custmor()
next(stall)
stall.send("Masala chai") 
stall.send("Lemon chai") 
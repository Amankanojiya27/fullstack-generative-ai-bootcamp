# Send Value to Generators

def chai_custmor():
    print("Welcome to chai shop !")
    order = yield              # receive first order
    while True:
        print(f"Preparing: {order}")  # process order
        order = yield          # wait for next order

stall = chai_custmor()
next(stall)                    # start generator
stall.send("Masala chai")      # send first order
stall.send("Lemon chai")       # send next order

# Yield From and Close the Generators

def local_chai():
    yield "Masala Chai"     # local option
    yield "Ginger Chai"
    
def imported_chai():
    yield "Matcha"          # imported option
    yield "Oolong"
    

def full_menu():
    yield from local_chai()     # delegate to local chai
    yield from imported_chai()  # delegate to imported chai

for chai in full_menu():
    print(chai)
    

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"  # wait for order
    except GeneratorExit:                          # handle close()
        print("still close, No more chai")
        
stall = chai_stall()
print(next(stall))   # start generator
stall.close()        # close generator and cleanup

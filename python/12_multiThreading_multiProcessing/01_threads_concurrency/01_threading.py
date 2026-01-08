import threading
import time
# threading → allows multiple tasks to run at the same time
# time → used to pause execution for a few seconds


def take_order():
    # This function simulates taking customer orders
    for i in range(1,4):  # Loop runs 3 times (order 1 to 3)
        print(f"Taking order No. #{i}")  # Display current order number
        time.sleep(2)  # Pause for 2 seconds to simulate time taken to take an order


def brew_tea():
    # This function simulates brewing tea
    for i in range(1,4):  # Loop runs 3 times (tea 1 to 3)
        print(f"Brewing tea of #{i}")  # Display which tea is being brewed
        time.sleep(3)  # Pause for 3 seconds to simulate brewing time
        

# Create threads
# A thread is a lightweight process that runs a function independently
order_thread = threading.Thread(target=take_order)  # Thread for taking orders
brew_thread = threading.Thread(target=brew_tea)     # Thread for brewing tea


# to invonk or start the thread 
# start() begins execution of the thread
order_thread.start()
brew_thread.start()


# wait for both to finish
# join() makes the main program wait until the threads complete
order_thread.join()
brew_thread.join()


# This line runs only after both threads have finished
print("All Order taken and Tea brewed")

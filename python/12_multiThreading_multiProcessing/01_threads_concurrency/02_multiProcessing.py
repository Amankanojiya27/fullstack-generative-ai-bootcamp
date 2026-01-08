# Import Process class to create separate processes (parallel tasks)
from multiprocessing import Process
import time  # Used to pause execution (sleep)

# This function will run in a separate process
def brew_tea(name):
    # Print when tea brewing starts
    print(f"Start of {name} tea Brewing")
    
    # Simulate time taken to brew tea (3 seconds)
    time.sleep(3)
    
    # Print when tea brewing ends
    print(f"End of {name} tea Brewing")

# This block ensures code runs only when the file is executed directly
# (Required for multiprocessing, especially on Windows)
if __name__ == "__main__":

    # Create a list of Process objects
    # Each process will run brew_tea() with a different name
    chai_makers = [
        Process(
            target=brew_tea,                 # Function to run in the process
            args=(f"chai maker #{i+1}",)      # Arguments passed to the function (tuple)
        )
        for i in range(3)                     # Create 3 processes
    ]
    
    # Start all processes
    # This actually begins parallel execution
    for p in chai_makers:
        p.start()
        
    # Wait for all processes to finish
    # join() blocks until each process completes
    for p in chai_makers:
        p.join()
    
    # This line runs after all processes are finished
    print("All tea brewing complete")

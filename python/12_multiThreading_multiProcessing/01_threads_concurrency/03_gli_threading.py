# The Global Interpreter Lock (GIL) in Python is like a single-lane tunnel for your program's threads, ensuring only one thread can run at a time, even on multi-core processors, to protect Python's memory management and prevent crashes from multiple threads accessing data simultaneously. This makes Python's threading simple but creates a bottleneck for CPU-heavy tasks, as threads must wait for their turn in the tunnel, preventing true parallel execution on multiple cores

# 03_gli_threading.py

import threading
import time


def brew_tea():
    print(f"{threading.current_thread().name} Start Brewing...")
    count =0
    for _ in range(100_00_000):
        count += 1
    print(f"{threading.current_thread().name} Finished Brewing...")

thread1= threading.Thread(target=brew_tea, name= "test-1")
thread2=  threading.Thread(target=brew_tea, name= "test-2")


start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()

print(f"total time taken: {end - start:.2f} second")
import threading
import time 

def boil_milk():
    print(f"{threading.current_thread().name} Start Boiling...")
    print(f"Start Boiling milk...")
    time.sleep(2)
    print(f"Finished Boiling milk...")

def toast_bun():
    print(f"{threading.current_thread().name} Start Toasting...")
    print(f"Toasting bun...")
    time.sleep(3)
    print(f"Finished Toasting bun...")

# boil_milk()
# toast_bun()


start = time.time()

thread1 = threading.Thread(target=boil_milk)
thread2 = threading.Thread(target=toast_bun)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()

print(f"Breackfast ready in: {end - start:.2f} second")





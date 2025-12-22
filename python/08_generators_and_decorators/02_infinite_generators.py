# Infinite Generators

def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"   # generate refill count
        count += 1

user1 = infinite_chai()           # first generator
user2 = infinite_chai()           # second generator

print("user1")
for _ in range(5):
    print(next(user1))            # get next refill
    
print("\n")

print("user2")
for _ in range(6):
    print(next(user2))            # independent sequence

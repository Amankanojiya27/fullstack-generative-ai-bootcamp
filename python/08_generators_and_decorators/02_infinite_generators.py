# Infinite Generators
def infinite_chai():
    count =1
    while True:
        yield f"Refil #{count}"
        count +=1

user1 = infinite_chai()
user2 = infinite_chai() 

print("user1")
for _ in range(5):
    print(next(user1))
    
print("\n")

print("user2")
for _ in range(6):
    print(next(user2))
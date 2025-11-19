# value = 13
# remainder = value % 5

# if remainder:
#     print(f"No divivible, remainder is {remainder}")

# := Walrus Operator
value = 13

if (remainder := value % 5 ):
    print(f"No divivible, remainder is {remainder}")

print("\n")
available_size = ["small","large","big"]
if (request_size := input("Enter your chai cap size: ").lower()) in available_size:
    print(f"Serving {request_size} chai cup")
else:
    print(f"Size is unavailable")


print("\n")
flavours = ["masala","lemon","ginger","mint" ]

while (flavour := input("Enter Your Flavour: ").lower()) not in flavours:
    print(f"{flavour} is not available")
else:
    print(f"{flavour} will be sever")
flacours = [ "vanilla", "chocolate", "out of stock","strawberry", "mint", "discontinue" ]

for flavour in flacours:
    if flavour == "out of stock":
        continue
    if flavour == "discontinue":
        break
    print(f"{flavour} item found")

print(f"{flavour} ")
        
    
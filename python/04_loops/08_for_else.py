staff = [("Amit",16),("Akash",29),("Ankit",21)]

for name,age in staff:
    if age > 30:
        print(f"{name} is too old")
        break
else:
    print(f"you all are young")
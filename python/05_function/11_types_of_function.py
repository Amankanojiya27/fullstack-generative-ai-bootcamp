# ------------------------------------------
def pure_chai(cups):
    return cups * 10
# ------------------------------------------

total_chai = 0
# not recommened , because it changing value of globle variable , its not good practice
def impure_chai(cups):
    global total_chai
    total_chai +=cups
    
# ------------------------------------------
print("\n")
#  Recursive functions
def pour_chai(n):
    print(n)
    if n==0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))
# ------------------------------------------
print("\n")
# Lambda (Anonymous function)
chai_type= ["light","kadak","kadak","ginger"]

strong_chai = list(filter(lambda chai: chai != "kadak",chai_type))
print(strong_chai)
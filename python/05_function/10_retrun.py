#----------------------------------------------------------
# ver 1
# def make_chai():
#     return "Here is Your Masala chai"

# return_value= make_chai()
# print(return_value)

# ver 2
def make_chai():
    print("Here is Your Masala chai")

return_value= make_chai()
print(return_value)
#----------------------------------------------------------

# ver 1
def idle_chaiwala():
    pass
print(idle_chaiwala())

# ver 2
def idle_chaiwala():
    pass
return_value = idle_chaiwala()
print(return_value)
#----------------------------------------------------------
print("\n")
def sold_cups():
    return 120
total_cup = sold_cups()
print(total_cup)
#----------------------------------------------------------
print("\n")
def chai_status(cup_left):
    if cup_left == 0:
        return "Sorry, Chai over"
    return "Chai is ready"
print(chai_status(0))
print(chai_status(5))
#----------------------------------------------------------

print("\n")
def chai_report():
    return 100,20 # sold, remaining

sold, remaining = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)
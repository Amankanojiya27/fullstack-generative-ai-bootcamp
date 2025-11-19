# -------------------------------------------- 
# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing ",order )
    
# prepare_chai(chai)
# print(chai)

# -------------------------------------------- 

chai = [1,3,4]
def edit_chai(cup):
    cup[0]= 42

edit_chai(chai)
print(chai)

# -------------------------------------------- 

#args
def make_chai(tea,milk,suger):
    print(tea,milk,suger)

make_chai("Masala","Yes","Low") #positional
make_chai(tea="Green",suger="Medium",milk="No") #keyword
# output :
# Masala Yes Low
# Green No Medium

# -------------------------------------------- 
print("\n")

# *kwargs
def special_chai (*ingredients, **extra):
# def special_chai (*args, **kwargs):
    print("Ingredients",ingredients)
    print("Extra",extra)

special_chai("Cinnamon", "Cardmon", sweetner="Honey", foam="Yes")
# output : 
# Ingredients ('Cinnamon', 'Cardmon')
# Extra {'sweetner': 'Honey', 'foam': 'Yes'}



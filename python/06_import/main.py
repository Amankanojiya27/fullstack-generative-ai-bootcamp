# ----------------

import recipes.flavor 
print(recipes.flavor.elachai_chai())

# ----------------

from recipes.flavor import elachai_chai, ginger_chai

print(ginger_chai())
print(elachai_chai())

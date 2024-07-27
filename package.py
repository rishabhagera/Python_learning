# a package is a collection(container) of modules
# in file system package is a [directory or a folder]


#importing package from ecommerce folder 
#we have maded a package 

import ecommerce.shipping
ecommerce.shipping.calc_shipping()

print("\n ")
#another method
from ecommerce.shipping import calc_shipping
calc_shipping()

print("\n")

#another method
from ecommerce import shipping
shipping.calc_shipping()


#importing functions directly from another files

"""
from modules import find_max

list=[10,30,11,78,231,1111,23,75,1221,3,4,6]
maximum=find_max(list) 
print(maximum)

#by build in function MAX
#print(max(list))

"""

#import modules
import modules
list=[10,30,11,78,231,1111,23,75,1221,3,4,6]
#from modules import lbs_to_kg,kg_to_lbs
# lg=lbs_to_kg(70)
# wg=kg_to_lbs(70)
# print(wg,lg)
maximum = modules.maximum(list)
print(f"maximum :{maximum}")
 



# Legal variables
"""
cold = True
cold_erry = True
_cold_erry = True
coldErry = True
COLDERRY = True
COLD_ERRY = True
"""

# Illegal Variables
"""
1cold = False
cold-erry = False
cold erry = False
""" 

# Multi Word var names

"""
Camel Case
- Each word except the first starts with a capital letter
"""
iAmNoob = True
"""
Pascal Case
- Each word starts with a capital letter
""" 
IAmNoob = True
"""
Snake Case
- Each word is reparated by underscore character
"""
i_am_professional = False

# Assign multi vars

a, b , c , d = "Colderry", "Lucid", "J_DDev", "RAD"
print("My besties")
print("- " + a)
print("- " + b)

# Global variables
def func ():
    global henlo
    henlo = "Henlo World"
# The function need to be called otherwise it will error
func()
print(henlo)

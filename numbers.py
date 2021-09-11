"""
Three numeric types in Python
- Int
- Float
- Complex
"""

"""
Int
- is positive or negative number without decimals
"""
this_is_int = 1
print(this_is_int)
print(type(this_is_int))

"""
Float
- is positive or negative number containing one or more decimals
"""
this_is_float = 1.0
print(this_is_float)
print(type(this_is_float))

"""
Complex
- Numbers are written with a "j" as the imaginary part 
"""
this_is_complex = 10j
print(this_is_complex)
print(type(this_is_complex))

# Type conversion

a = int(this_is_float)
b = float(this_is_int)
c = complex(this_is_int) # Note you can't convert complex into another number type

# Random number
import random # Import random module

print(random.randrange(1, 1000)) # Get random number between 1 and 1000

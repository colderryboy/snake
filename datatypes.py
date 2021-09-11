"""
1. Text type: "str"
2. Numeric types: "int", "float", "complex"
3. Sequence types: "list", "tuple", "range"
4. Mapping types: "dict - replace t with k lol"
5. Set types: "set", "frozenset - TF"
6. Boolean type: "bool"
7. Binary types: "bytes", "bytearray", "memoryview"
"""

# Str
str = "Henlo World"
print(type(str))

# Int
int = 10
print(type(int))

# Float
float = 10.42
print(type(float))

# Complex
complex = 5j
print(type(complex))

# List
list = ["Colderry", "Lucid", "J_DDev"]
print(type(list))

# Turple
turple = ("Colderry", "Poggers")
print(type(turple))

# Range
r = range(69)
print(type(r))

# Dict
dict = {"username": "Colderry", "id": 123456 }
print(type(dict))

# Set
set = {"Colderry", "21525245"}
print(type(set))

# Frozen Set
fset = frozenset({"Colderry", "123456"})
print(type(fset))

# Bool
bool = True
print(type(bool))

# Bytes
byte = b"Henlo"
print(type(bytes))

# Bytearray
barray = bytearray(69)
print(type(barray))

# Memoryview
mview = memoryview(bytes(69))
print(type(mview))

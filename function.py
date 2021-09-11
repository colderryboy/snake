word = "milk"

def func():
    print("Snake needs some " + word)

func()

# With argument
def func_2(a):
    print("Snake needs some " + a)

func_2(word)
"""
If we try to call the function with 2 args it will error
func_2(word, "error")
"""

# Arbitrary args
def func_3(*names):
    print("Name " + names[2])

func_3("1", "2", "Colderry")

# Keyword args
def func_4(ar1, ar2, ar3):
    print("The ar3 is " + ar3)

func_4(ar3 = "Colderry", ar2 = 0, ar1 = 45245245)

# Arbitrary keyword args
def func_5(**name):
    print("Name: " + name["yes"])

func_5(yes = "Colderry")

# Default value
def func_6(key = "f"):
    print("Press " + key + " to pray respects")

func_6()

# List
def func_7(words):
    for w in words:
        print("Word: " + w)

func_7(["decent", "fine", "yes"])

# Return value

def func_8(number):
    return 69 - number

print(func_8(68))

# Pass statement when no content
def func_9():
    pass

func_9()

# Recursion
print("Confusing so I skipped")

# VARS are CASE SENSITIVE

# declare
x = "lala"
# specify type
y: str = "1234"

# cast
z = int(y)
f = float(y)
z = str(z)

# get type
print(type(f))

# PRINT variables
print("variable x is ", x)

# string formatting using % or {}
print("variable x using perc is %s" %(x))
print("variable x using brackets is {}".format(x))
print("variable x using brackets and + is {} " + x)

# using f-string
print(f"using f variable x is {x}")


# BOOL values
"""
most values TRUE if they have some content
strings are TRUE if not empty
ints are TRUE if not 0
list, tuple, set and dict are TRUE if not empty
"""
bool("abc")
bool(10)



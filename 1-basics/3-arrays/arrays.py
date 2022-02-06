
array = ["a", "b", "c", 1, 2]

# length
print(len(array))

# element
print(array[1])

#modify
array[0] = "x"

#loop
for x in array:
    print(x)

# add to end of an array
array.append("zzz")
print(array)

# remove item on index or by value
array.pop(0)
array.remove("c")
print(array)
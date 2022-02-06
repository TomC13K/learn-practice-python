# comment
"""
Multiline
comment - python ignores strings not assigned to variable
"""

simple_string: str = "Hello World"

multiline_string: str = '''Something
over multiple
lines'''

print(simple_string)
print(multiline_string)

# LENGTH STRING
print(len(simple_string))

# STRING ARRAY
#print(simple_string[0])

# STRING LOOP
#for str in simple_string:
#    print(str)


# WORD SEARCH in string
# case sensitive !
search_word = "World" in simple_string;
not_existing_word = "Seven" not in simple_string
print(search_word)

if search_word :
    print("Text contains a word World")

if not_existing_word :
    print("Text doesnt contains a word Seven")

# SLICING
# from start first 3 chars
print(simple_string[:3])

# word AFTER the first 2 chars
print(simple_string[2:])

# slice between position [indexes!]   last is not included in output
print(simple_string[0:2])

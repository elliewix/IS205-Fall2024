print(1) # this in an int
print("1") # looks similar but is text
print("this is as string")

print(type(1)) # should see int
print(type('1')) # should see str for string

print(type) # funky output
print(type(print)) # funky output

# variables and assignments

x = 4 # just saving a random number
print(x + 3) # printing a calculation
x = 4 + x # updating a variable's assignment
print(x) # and printing the new value

y = 1 + x

# can't use reserved words like True etc.
# shouldn't use things without meaning
# this thing = 4 # nope, can't have a space

this_thing = 4 # okay, but not descriptive?

print(x == 4) # this is equality
# print(x = 4)
print(x)

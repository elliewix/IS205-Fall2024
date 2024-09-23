# write a function that returns a greeting
# call it greeting, takes a string with a name
# returns the greeting

# getting started template
def greeting(name):
    # do stuff here
    greeting = "" # give yourself a placeholder
    return greeting

# and then start filling in

def greeting(name):
    # do stuff here
    greeting = "hello " + name # give yourself a placeholder
    return greeting

print(greeting("A Human"))


### importing modules

# random module, as an example
## import module_name
import random

print(random.choice("hello"))

## import with an alias

import random as rd # I made this up, don't use it

## can't use random anymore
print(rd.choice("hello"))

# or you can import just a function
# this is to be used for just specific needs
from random import choice

print(choice("hello"))

# or these extremely sus
from random import *

print(choice("hello"))

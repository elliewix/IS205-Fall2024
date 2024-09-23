# importing modules

## import the module by name

import random

# use random before all function names

print(random.choice("hello"))

# import the module with an alias
# giving it a nickname
# eg import pandas as pd

import random as rd # I made up, just use import random
# now random.choice() won't work
print(rd.choice("hello"))

from random import choice
# imports just choice
# and you don't have to use random. before it

print(choice("hello"))

# extremely sus
from random import *

print(choice("hello"))

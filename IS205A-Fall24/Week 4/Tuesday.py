# defining functions

# let's start with basics functions first

## a few we already know

# print("will show stuff for us")
# print(sum([1,2,3]))
# print(min(1,2,3))
# print(len("hello"))

# how do you start on a function?

## answer some questions

## 1) what should the name be?
## 2) what inputs should it get?
## 3) what should it do?
## 4) what should it return?

## let's do this together

## 1) what should the name be?
# add_these
## 2) what inputs should it get?
# two numbers, x and y and will be int or float
## 3) what should it do?
# add x and y together
## 4) what should it return?
# the sum

# so now putting this is code

def add_these(x, y):
    # x and y with be defined for you
    # when the function starts
    result = x + y     # do stuff, #3
    return result # return the value, #4

# now you can call the function
# be sure it is outside the function block
# and you use print
print("the sum of these numbers is")
print(add_these(1, 2))
print("but sometimes not sum....")
print(add_these("cats", "dogs"))

# you can combine and say
x = "silly things here"

print("the sum is", add_these(2,10))

def greeting(name):
    result = "hello there, " + name
    return result

print(greeting("Student"))
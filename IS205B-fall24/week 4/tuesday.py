# we've done functions before

print("hello there humans")
print(len("hello"))

## 1) what should the name of the function be?
## 2) what should the inputs be? what does the function
##      need to know about? and their names?
## 3) what should it do? what it's reason for living?
## 4) what should it return?

## do it in action


## 1) what should the name of the function be?
# add_these
## 2) what should the inputs be? what does the function
##      need to know about? and their names?
# the two numbers, x and y
## 3) what should it do? what it's reason for living?
# add the numbers together
## 4) what should it return?
# the sum

# now the syntax

def add_these(x, y):
    # 3 doing stuff happens here
    result = x + y
    # 3 finish doing stuff
    return result # 4

print("the sum is")
print(add_these(1, 2))
print("another sum is", add_these(4, 5))
# loops, specifically for loops

# we start with an object

s = "hello"

# this object has a data type
# in the case, a string
# strings unpack as characters
# individual characters
# so, "hello" would have h e l l o

# to loop over a string, this will isolate
# each character, one at a time, for you to do
# ~~~whatever~~~ to. this being your problem solving

for character in s:
    print(character)

# "character" here is a variable you define
# I call it the iterable variable
# the name doesn't matter, but name it something
# reasonable or else suffering....

for c in s:
    print(c) # will give the same results

# another example of how the iterable variable name
# doesn't matter, except for human readability

for a_number in s:
    print(a_number) # still a string lol

# let's talk about split

sentence = "hello there humans."
# for our purposes, to get the words
# out of this, we used .split()

words = sentence.split()
print(words) #caution, words is now a list

for w in words:
    print(w)
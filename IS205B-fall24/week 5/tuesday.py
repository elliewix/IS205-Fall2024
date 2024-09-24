# for loops
# you start a sequence or collection of stuff
# and that object will spit out stuff as
# you loop over it
# the data type of the thing your are looping over
# dictates what comes out of that thing


# for example, strings will unpack as characters

s = "hello" # this is a string

# for iterable_variable in sequence....

for character in s:
    print(character)
# the content of the iterable var doesn't matter
# it just needs to be reasonable
for c in s:
    print(c)
for absolutely_a_number in s:
    print(absolutely_a_number) # lol still a string tho

## using split and string methods

sentence = "hello fellow humans."
words = sentence.split()
print(words)

# looping over a list
# be mindful, the content coming out of the list will
# likely be a diff data type

for w in words: # see how the syntax is the same?
    print(w)

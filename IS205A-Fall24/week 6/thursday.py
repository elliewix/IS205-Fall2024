words = ["hello", "fellow", "human", "entities", "y'all", "are", "cool"]

# if we want one element from this list
# we use indexing
# index positions start at 0

print(words[0]) # should be "hello"
print(words[2]) # should be "human"

# indexing gives you the exact thing from
# the sequence


# slicing is diff, you work in groups
# [start:stop] start inclusive, stop exclusive
# similar to [start, stop) if you know that syntax from math
print(words[1:5]) # will give me 1th, 2th, 3th, and 4th items

# what if you leave things out?

print(words[:3]) # presumes from the start
print(words[4:]) # presumes to the end

# negative indexing does work

print(words[-1])

## reading files a bit diff

infile = open('somestuff.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

print(text) # this gives us everything from the file

# alternatively go line by line
# not your default way of going about it

infile = open('somestuff.txt', 'rt', encoding='utf-8')

# you can loop over infile, getting one line
# as a string in each run of the loop
# only saves one line at a time in the iterable
# but does require that you do a bit more work
# to do what you need
for line in infile:
    print(line)

infile.close()
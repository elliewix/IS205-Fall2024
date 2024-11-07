some_words = "here are some words humans"

# don't really want to do this...

h_count = 0
e_count = 0
r_count = 0
# etc....

for letter in some_words:
    if letter == "h":
        h_count = h_count + 1
    elif letter == "e":
        e_count = e_count + 1
    elif letter == "r":
        r_count = r_count + 1
    # etc....
print(h_count, e_count, r_count)

## creating an empty dictionary

d = {}
# add a key and value to it

d['a'] = 0
print(d)

# update the value of a
# change it to 4
d['a'] = 4
print(d)

# increment a current value

d['a'] = d['a'] + 1
print(d)

## let's count the letters automatically
# dict accumulator pattern, roughly
# used when you want it to automatically grow for all
# the things.
# eg count all the words
sentence = "apples and bananas"

letter_counts = {}

for letter in sentence:
    if letter in letter_counts: # if it's already in there
        # increment up
        letter_counts[letter] = letter_counts[letter] + 1
    else: # hasn't seen it, new key
        letter_counts[letter] = 1
print(letter_counts)

# alternative variation, used when you're looking
# only for specific things, eg only certain terms
sentence = "apples and bananas"
letter_counts = {}
terms = ['a', 'n', ' ']
# prepopulate a dictionary
for t in terms:
    letter_counts[t] = 0 # creating all the keys set to 0
print(letter_counts)
for l in sentence:
    if l in letter_counts:
        letter_counts[l] = letter_counts[l] + 1

print(letter_counts)

# looking at things in a diff way
# CAUTION don't use this pattern for hw4
# see things in a nested loop

for t in letter_counts:

    for l in sentence:
        print(t, l)


## change gears, class challenge

# create an empty dictionary called counts

counts = {}

# create a sentence with some repeated words
# and split that sentence into words

text = "here here human here here cat why why why"
words = text.split()
print(words)

# create a list of the words to search for

terms = ["here", "why"]

# loop over your list of terms, and prepopulate a dictionary
# with those terms set to 0

for t in terms:
    counts[t] = 0

for t in terms:

    for w in words:
        # print(t, w)
        # caution don't use this for hw4
        if t == w:
            counts[t] = counts[t] + 1
print(counts)

#

d = {}

d['a'] = 0

print(d)
print(d['a'])
my_list = []
my_dict = {}

some_words = "here are some words humans"

a_count = 0
b_count = 0
c_count = 0
#......
for letter in some_words:
    if letter == "a":
        a_count = a_count + 1
    elif letter == "b":
        b_count = b_count + 1
    elif letter == "c":
        c_count = c_count + 1
    # ....
    # this is terrible

print(a_count, b_count, c_count)

# create an empty dictionary

d = {}

# add a key/value pair in
# dictionary_variable[key_content] = value
d['a'] = 0
# your keys will usually be strings
# your values can be any data type, but
# you should match that data type across the dict

print(d)

# updating or changing the value for a key

d['a'] = 3
print(d)

# incrementing a value in a dictionary for a key
# add 1 to the 'a' key

d['a'] = d['a'] + 1

print(d)

# loop over content and add it as keys
letters = ['a', 'b', 'c']

count_dict = {}
# prepopulate this dictionary with values
for l in letters:
    count_dict[l] = 0 # setting all values to 0
    print(count_dict)

# loop over a dictionary

for key, value in count_dict.items():
    print(key, value)

print(count_dict.items())

## let's some things together

for l in some_words:
    # print(l)
    # this will give an error
    # count_dict[l] = count_dict[l] + 1
    # we only want to count what's in our dictionary
    if l in count_dict:
        count_dict[l] = count_dict[l] + 1
    print(count_dict)

sentence = "hello again here are more words!!!"

counted_letters = {}
for l in sentence:
    if l in counted_letters: # if we've seen it before
        counted_letters[l] = counted_letters[l] + 1
    else: # we haven't seen it before, need to add
        counted_letters[l] = 1 # start at one because we're looking at one
    print(counted_letters)

# see the value of a specific key

print(counted_letters['o'])

# in class challenge
# 1) create an empty dictionary called counts

counts = {}

# write a sentence of your choice as a string
# and split it into words. save this list as words

sentence = "humans are animals and batteries are not"
words = sentence.split()

# loop over those words
# add an if statement to check if the words are longer
# than three characters, printing only those out
for w in words:
    if len(w) > 3:
        print(w)
# next phase, add only these words to your dictionary
# setting the value as 0
for w in words:
    if len(w) > 3:
        counts[w] = 0

# write a new sentence that repeats these words randomly multiple times

manywords = "humans humans humans batteries animals other animals things humans"
words = manywords.split()

for k in counts.keys():
    # print(k) # we see just the keys in our dictionary
    for w in words:
        # print(k, w)
        if k == w: # beware don't use this for hw4
            counts[k] = counts[k] + 1
print(counts)
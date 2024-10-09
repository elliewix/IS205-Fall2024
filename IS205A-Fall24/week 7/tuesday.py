# count the number of times something
# runs or executes or something

counter = 0 # integer accumulator
for i in range(10):
    if i % 2 == 0:
        # increment counter
        counter = counter + 1
        print(i, counter)
# see the result
print(counter)

# instead of counting, let's collect

# set the base of a list accumulator
all_my_numbers = []

for i in range(10):
    if i % 2 == 0: # checks if even number, sort of don't fight me
        all_my_numbers.append(i) # NO = ASSIGNMENT

print(all_my_numbers)

##

sentence = "here are many cats for you"
words = sentence.split()
# make these words exciting

exciting_words = []
for w in words:
    new_word = w + "!!" # putting some excitement in!
    exciting_words.append(new_word)

print(exciting_words)
# put a list of words back into a string
# use the join method
# call join on the connecting character, and give it the sequence
print("XXXXXXXX".join(exciting_words))
print(" ".join(exciting_words))


###

# write a function that take a line of text
# a returns how many words are in it
# call it count_words

def count_words(line_of_text):
    # do stuff here
    # remember this is meant to take a single string
    words = line_of_text.split()
    word_count = len(words)
    return word_count

print(count_words(sentence))

# let's read the file
# run each line through our function

infile = open('Three-years-in-europe.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

# get the lines out of text
# remember that text is just a big string of all the stuff
lines = text.splitlines()

for l in lines:
    # print(l) # always check what you are looping over
    if count_words(l) > 14: # pass our line into our function
        print(l)
# int accumulator
# also called a counter

# count how many even numbers there are

count = 0 # start our base

for i in range(10):
    if i % 2 == 0:
        count = count + 1 # increment the counter
        print(i, count)

print(count)

## list accumulator

all_even_numbers = []

for i in range(10):
    if i % 2 == 0:
        all_even_numbers.append(i)

print(all_even_numbers)

###
# write a function that takes in a line of text
# and counts the words in it, returns the number count
# call it count_words

def count_words(line_of_text):
    # do stuff
    words = line_of_text.split()
    word_count = len(words)
    return word_count

print(count_words("here are some cats for you"))

def make_exciting(line_of_text):
    words = line_of_text.split()
    new_words = []
    for w in words:
        w = w + "!!!"
        # print(w)
        new_words.append(w)
    new_line = " ".join(new_words)
    # call on the connecting text, give it the seq
    # print(new_words)
    return new_line
print(make_exciting("here are some cats for you"))

## read in a file

infile = open('Three-years-in-europe.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

lines = text.splitlines()

# print(lines)
for l in lines:
    # print(l) # always double check
    count = count_words(l)
    # print(count)
    if count > 16:
        print(l)
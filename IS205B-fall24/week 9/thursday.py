# general review of nested for loops

for letter in "XYZ":
    for number in [1,2,3]:
        print(letter, number)

import random
# outfile, and we want to write stuff to it from a for loop
# outfile as an accumulator pattern

words = ["cat", 'dog', 'apple']
# this is our base, before our for loop
outfile = open('mynewtext.txt', 'wt', encoding='utf-8')
# for loop writes stuff to the file
for w in words:
    outfile.write(w + "\n")
outfile.close()

## we want to make outfiles within a for loop

terms = ['dog', 'banana', 'snake', 'rubber']
# let's make one file for each term
for t in terms:
    fname = t + ".txt"
    print(fname)
    outfile = open(fname, 'wt', encoding='utf-8')
    outfile.write("here's a WORD: " + t)
    outfile.close()

## we need to make files but also use a for loop on the content

terms = ["letter", "ocean", "dog", "boat"]

for t in terms:
    fname = t + "-results.txt"
    print(fname)
    outfile = open(fname, 'wt', encoding='utf-8') # the base
    for letter in t:
        # print(letter)
        outfile.write(letter + '\n') #increment
    outfile.close()
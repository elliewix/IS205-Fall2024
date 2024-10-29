# seen nested earlier
import random
for letter in "XYZ":
    for number in [1, 2]:
        print(letter, number)

# files and for loops
## writing out a file with a for loop
# reviewing just one file
outfile = open('newtext.txt', 'wt', encoding='utf-8')
words = ["hello", "humans", "cats", "dogs"]
for i in range(5):
    pick = random.choice(words)
    outfile.write(pick + "\n")
outfile.close()

# now make files within a single for loop

make_these_files = ["snake", "banana", "apple"]

# let's make each word into a file
for word in make_these_files:
    # always print the filename before
    # you start making them
    fname = word + ".txt"
    print(fname)
    outfile = open(fname, 'wt', encoding='utf-8')
    outfile.write("here's a word: " + word)
    outfile.close()


## make files but with a nested loop

for word in words:
    fname = word + "-results.txt"
    print(fname)
    # base outfile
    outfile = open(fname, 'wt', encoding='utf-8')
    for letter in word:
        print(letter)
        outfile.write(letter + "\n") # increment
    # close/wrapup
    outfile.close()

import random
import string

letters = string.ascii_letters
print(letters)
# this is what we want to do
# we now want the output of this to
# be written out to a file instead
# of just printing to screen
for i in range(20):
    new_word = random.choices(letters, k = 5)
    # print("".join(new_word))

# take this and add the outfile pattern around it
# note stuff goes inside and outside of the for loop
# use a file name that's new! not your
# current data
outfile = open('mynewdata.txt', 'wt', encoding='utf-8') # the base of our file
for i in range(20):
    new_word = random.choices(letters, k = 5)
    print("".join(new_word)) # change the print here
    # outfile.write("".join(new_word)) # writes one line
    # oops, everthing was just in one line
    # I need to add a newline character
    outfile.write("".join(new_word)) # writes one line

outfile.close()
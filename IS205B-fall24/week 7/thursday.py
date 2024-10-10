import random
import string

letters = string.ascii_letters
print(letters)

# our original work where we can see the stuff and just
# printing it out
# this is the point where I can start writing things out
for i in range(20):
    random_letters = random.choices(letters, k = 5)
    # print(random_letters)
    random_word = "".join(random_letters)
    # print(random_word)

# new we can add the code in to write the file
# note the outfile pattern will have stuff inside
# and outside of the for loop

outfile = open('mynewfile.txt', 'wt', encoding='utf-8')

for i in range(20):
    random_letters = random.choices(letters, k = 5)
    # print(random_letters)
    random_word = "".join(random_letters)
    print(random_word + "\n")
    # now "increment" the content
    outfile.write(random_word + "\n")

# now close the file
outfile.close()
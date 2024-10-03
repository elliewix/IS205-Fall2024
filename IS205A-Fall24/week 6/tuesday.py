sentence = "scattered around here are some cats that are catalytic"

print("cat" in sentence)

words = sentence.split()

# for w in sentence: # not looping over the string,
#     print(w)

for w in words: # we want to loop over the list of words
    # print(w)
    # print("cat" in w, w)
    # if ("cat" in w) == True: # finds all the cat ones
    # if ("cat" in w) == False: # all the words that don't
    #     print(w)
    # if ("cat" in w):
    #     print(w)
    # else:
    #     print("not a cat word")
    if w.startswith("cat") == True:
        print("starts with it")
    elif ("cat" in w) == True:
        print("has cat inside, but doesn't start with")
    else:
        print("no cat at all")


## files!

# let's read in a file
# first step, tell python ABOUT the file

infile = open('somestuff.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

# infile is done, we just have tet now

print(text)
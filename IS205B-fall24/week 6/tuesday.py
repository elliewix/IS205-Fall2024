sentence = "critical scattered cats have cathartic play time"

print("cat" in sentence)
# print out the words that have cat in them

words = sentence.split()

# for w in words:
#     print(w)

# vs...why we check the work
# for w in sentence:
#     print(w)

# for w in words:
    # print("cat" in w, w) # printing it is good, but let's do more
    # if ("cat" in w) == True:
    #     print(w)
    # else:
    #     print("no cat found")

for w in words:
    if w.startswith("cat"):
        print(w, "starts with cat")
    elif "cat" in w:
        print(w, "cat inside, but doesn't start with")
    # and for everything else
    else:
        print("doesn't have cat")

### working with files, mostly reading them in for now

infile = open('somestuff.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

print(text)
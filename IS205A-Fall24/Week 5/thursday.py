
# meet the in keyword
# checks for membership
# works diff for diff data types
# strings, looks for substrings
# lists, looks for exact matches
example_sentence = "This is the story of humans and stuff."

result = "cat" in example_sentence
print(result)
print("man" in example_sentence) # True, but maybe not what we wanted

print(example_sentence.split())

# in will work with lists, BUT it only looks for exact matches
print("man" in example_sentence.split()) # False, like I wanted

# so that's better, but still not great

print("stuff" in example_sentence.split()) # wanted True...but false
print("stuff." in example_sentence.split()) # Now we see True
print("this" in example_sentence.split()) # False, becasue T

# hmm let's lowercase everything

lower_sen = example_sentence.lower()
lower_word = "This".lower()

print(lower_word in lower_sen.split())

## let's deal with punctuation

new_sentence = "Mr. Mime, Jr. (045) is a Pokemon."
new_sentence = new_sentence.lower()
split_sen = new_sentence.split() # cool but still has punc
print(split_sen)
# let's deal with that now

# replace(...) string method

# this just does one but we want to automate it...
# clean_sen = new_sentence.replace(".", "")
# print(clean_sen)

import string

print(string.punctuation)
# remember that new_sentence was lowercased earlier
for punc in string.punctuation:
    # print(punc)  # always print the iterable first
    # so cool, this does it but isn't saving
    # print(new_sentence.replace(punc, ""))
    # so we need to save it
    # we can do this with iterative reassignment/assignment
    new_sentence = new_sentence.replace(punc, "")
    print(new_sentence)
    # remember new_sentence was created and lives outside

# now that it's cleaned, we can try split again

split_sen = new_sentence.split()
print("mime" in new_sentence)
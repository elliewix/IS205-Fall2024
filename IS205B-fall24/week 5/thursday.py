sentence = "hello fellow humans, there."

# let's meet the in keyword
# when you use in on a string, it looks for substrings

print("cat" in sentence) #False
print("man" in sentence) # True, because it's in human

sen = "Mr. Mime, Jr. (045) is a pokemon."
print("mime" in sen) # False, but we wanted True, so we need to change case
word = "mime"
sen = sen.lower() # update to be lowercase
word = word.lower() # same thing
print(sen)
print(word in sen) #True now!
word = "poke"
print(word in sen) # still true though

# let's look at in with lists

# remember than split changes a string to a list, broken up
sen_words = sen.split() # already lowercased from before
print(sen_words)
# in keyword with a list checks for exact matches
print("poke" in sen_words) # false!
print("mime" in sen_words) # True

# okay so still not theree....
# let's go back to the sentence

print(sen)

import string
print(string.punctuation)
print("hello!!!!..qqqu..pp())".replace(".", ""))

for punc in string.punctuation:
    # print(punc) # always print the iterable first
    # print(sen.replace(punc, ""))
    # you might to save this as
    # fixed = sen.replace(punc,"")
    # print(fixed)
    # nope, we iteratively update the existing variable
    sen = sen.replace(punc, "")
    print(sen)

# go back to the start and see what happens
sen_split = sen.split()
print(sen_split)
print("mime" in sen_split)
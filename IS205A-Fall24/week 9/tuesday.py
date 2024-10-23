# playing with nested loops first

for letter in "ABC": # outer loop
    for number in [1,2,3]: # inner loop
        # print(letter, number)
        print(number, letter)

for number in [1,2,3]:
    for letter in "ABC":
        print(number, letter)

text = """here is some text
not about cats
super not about cats at all"""

print(text)
lines = text.splitlines()
print(lines)
for l in lines:
    # print(l)
    words = l.split()
    print(words)
    for w in words:
        print(w)

#

text = """here is some text
not about cats
super not about cats at all"""

# let's calculate the mean length of words
# inside of each line

lines = text.splitlines()
for l in lines:
    words = l.split() # will give me a list of words
    num_words = len(words)
    # print(num_words, words)
    num_letter_per_line = 0 # base for the inner loop
    for w in words:
        # print(len(w), w)
        num_letter_per_line = num_letter_per_line + len(w)
    # to see results, print outside of and after for loop
    # see the indent?
    # print(num_words, num_letter_per_line, l)
    print(l, num_letter_per_line / num_words)
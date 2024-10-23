# a plain nested for loop

for letter in "ABC": # outer loop
    for number in [1,2,3]: # inner loop
        print(letter, number)

print("the other loop")
for number in [1,2,3]:
    for letter in "ABC":
        print(letter, number)

## an actual example

# what is the mean length of the words in each line?

text = """here is some text
totally not about cats
super not about cats at all"""

lines = text.splitlines()
# print(lines)

for l in lines:
    # print(l)
    words = l.split()
    word_length = len(words)
    print(word_length, words)
    letter_sum = 0 # base
    for w in words:
        # print(w)
        num_letters = len(w)
        # print(num_letters)
        letter_sum = letter_sum + num_letters
    print(word_length, letter_sum, letter_sum/word_length)

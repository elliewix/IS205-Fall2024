counts = {'a': 4, 'b': 3}
print(counts['a'])
print(counts['b'])

pets = ['cat', 'cat', 'dog', 'fish']

pet_data = {'participant 1': {'pet_count': 0,
                              'pet_kinds': []}}

## brief intermission the shorthand
a = 0
a = a + 1 # increment up pattern
b = 5
b += 1 # same thing
print(a, b)

### done

print(pet_data)
# get the count
print(pet_data['participant 1'])
print(pet_data['participant 1']['pet_count'])
# because its just a number now, we can do math
print(pet_data['participant 1']['pet_count'] + 1)
# do the math but save the value
pet_data['participant 1']['pet_count'] += 1
print(pet_data)
# now let's think about the list
print(pet_data['participant 1']['pet_kinds'])
pet_data['participant 1']['pet_kinds'].append("cat")
print(pet_data)

#### let's make some random data
import random
random.seed(3)
pet_options = ['cat', 'dog','fish', 'snake']

all_pets = []
for apt_num in range(5):
    number_of_pets = random.randint(0, 5)
    pets = []
    for p in range(number_of_pets):
        pets.append(random.choice(pet_options))
    all_pets.append(pets)

print(all_pets)

pet_details = {}
for apt_number, pets in enumerate(all_pets):
    # print(apt_number, pets)
    unit_number = "Unit " + str(apt_number)
    # print(unit_number)
    pet_details[unit_number] = {'pet_counts': 0,
                                'pet_kinds': []}
    for p in pets:
        # hw5 would have an if statement here.....
        pet_details[unit_number]['pet_counts'] += 1 # integer
        pet_details[unit_number]['pet_kinds'].append(p) # this is a list!
print(pet_details)
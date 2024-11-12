# seen dicts with counters before

counts = {'a': 5, 'b': 2}
# see the values
print(counts['a'])
print(counts['b'])
# increment the values
counts['a'] = counts['a'] + 1
print(counts)

## let's add some complexity

pet_data = {}
pet_data['participant 1'] = {'pet_count': 0,
                             'pet_names': []}

print(pet_data)
print(pet_data['participant 1'])
print(pet_data['participant 1']['pet_count'])
# because we get a number we can do number things to it
# we didn't save this one though, just printed
print(pet_data['participant 1']['pet_count'] + 1)
# because we get a list back we can do list things
pet_data['participant 1']['pet_names'].append('fluffy')
print(pet_data)

##  prepopulation

cats = ['fluffy', 'flurry', 'zeb', 'mac']

pets = {'person 1': {'pet_count': 0,
                     'pet_names': []}}
print(pets)
for c in cats:
    pets['person 1']['pet_count'] = pets['person 1']['pet_count'] + 1
    pets['person 1']['pet_names'].append(c)
print(pets)

import random
random.seed(3)
pet_types = ['cat', 'dog', 'snake', 'fish']
all_pets = []
for unit_number in range(5): # have five entities
    number_of_pets = random.randint(0, 3)
    unit_pets = []
    for i in range(number_of_pets):
        unit_pets.append(random.choice(pet_types))
    all_pets.append(unit_pets)
print(all_pets)

pet_apt_data = {}

for unit_number, pets in enumerate(all_pets):
    key_id = "Unit " + str(unit_number)
    print(key_id, pets)
    pet_apt_data[key_id] = {'pet_count': 0,
                            'pet_kinds': []}
    for p in pets:
        pet_apt_data[key_id]['pet_count'] += 1 # this is an int counter
        pet_apt_data[key_id]['pet_kinds'].append(p) # this is a list
print(pet_apt_data)

# about the += thing

a = 0
a = a + 1

b = 0
b += 1
print(a, b)
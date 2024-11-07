import random
import csv

outer_data = []
animals = ['cat', 'dog', 'fish']
for i in range(3):
    round = i
    pet = random.choice(animals)
    count = random.randint(0,5)
    name = random.choice(animals) + ", " + random.choice(animals)
    # print(round, pet, count, name)
    row = [round, pet, count, name]
    outer_data.append(row)

print(outer_data)

# let's add some headers

headers = ['round', 'pet', 'count', 'name']

# now we have the data, let's write a csv

outfile = open('petdata.csv', 'wt', encoding='utf-8', newline = "")
csvout = csv.writer(outfile)
# write out the headers
csvout.writerow(headers)
# if we have a 2d array/list we can use writerows
csvout.writerows(outer_data) # plural!
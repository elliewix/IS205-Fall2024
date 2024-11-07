import random
import csv

# make some fake data
animals = ['dog', 'cat', 'fish']
outer_data = []
for round in range(3):
    choice = random.choice(animals)
    count = random.randint(0,5)
    name = random.choice(animals) + ", " + random.choice(animals)
    # print(round, choice, count, name)
    row = [round, choice, count, name]
    print(row)
    outer_data.append(row)

print(outer_data)

# boilerplate code for writing out a csv
headers = ['round', 'choice', 'count', 'name']

outfile = open('petdata.csv', 'wt', encoding='utf-8', newline="")
csvout = csv.writer(outfile)

# write the headers out
csvout.writerow(headers)
# write the 2d list to it
csvout.writerows(outer_data) # write the 2d list out
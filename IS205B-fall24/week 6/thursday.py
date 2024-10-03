l = ["hello", "there", "fellow", "human", "folk", "yay"]

print(len(l)) # measurement works as normal

# indexing, so give it the one index position
# and you get back that object
print(l[2]) # get fellow
# remember you get the ONE THING and it'll be that datatype

## slicing, so you get a group

# thing[start:stop] remember inclusive:exclusive

# if I wanted th 2th-4th items, inclusive
# I'd need 2:5
print(l[2:5])
# and I get back a list because I'm slicing a list

# if you omit start, it presumes beginning
print(l[:5])

# omit stop, and it presumes the end
print(l[5:])
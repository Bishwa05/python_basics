import modules

from modules import kg_to_lbs

print(kg_to_lbs(100))

print(modules.kg_to_lbs(72))

numbers = [10,3, 6, 7, 85]

print(modules.find_max(numbers))

# Build in function max
print(max(numbers))

# Build-in modules
# python 3 module index search in google

import random

for i in range(3):
    print(random.random())
    print(random.randint(10,20))

# select a leader randomly
members =['John', 'Mary', 'Bob', 'Bishwa']
leader = random.choice(members)
print(leader)


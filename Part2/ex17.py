import random

# 1. Ask the user for their name
name = input("What is your name? ")

# 2. Define the adjective and animal lists
adjectives = ['Sneaky', 'Brave', 'Silent', 'Swift', 'Witty', 'Fierce']
animals = ['Tiger', 'Otter', 'Falcon', 'Panther', 'Wolf', 'Fox']

# 3. Pick a random adjective and animal
random_adjective = random.choice(adjectives)
random_animal = random.choice(animals)

# 4. Combine them to make a codename
codename = random_adjective + " " + random_animal

# 5. Generate a random lucky number from 1 to 99
lucky_number = random.randint(1, 99)

# 6. Print the final message
print("Welcome, Agent " + name + ".")
print("Your codename is: " + codename)
print("Your lucky number is: " + str(lucky_number))

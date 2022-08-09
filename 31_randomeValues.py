import random


class Dice:
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)
#first = random.randint(1, 6)
#second = random.randint(1, 6)
#return first, second

dice = Dice()
print(dice.roll())


"""
for i in range(3):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)
"""
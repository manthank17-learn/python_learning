import random

trials = 100000
matches = 0

for _ in range(trials):

    birthdays = []

    # create 23 birthdays
    for i in range(23):
        birthdays.append(random.randint(1, 365))

    # check duplicates
    if len(birthdays) != len(set(birthdays)):
        matches += 1

print(matches / trials)
"""
Q 1.29 Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once. """

# for i in range()

"""
P-1.30 Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2."""


def num_div_two(num):
    times = 0

    while True:
        print(f"{num} / 2 = {num // 2}")
        num //= 2
        times += 1
        if num < 2:
            break
    return times


# print(num_div_two(10))

"""
P-1.31 Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to ddesign your program so that it returns as
few bills and coins as possible."""


def changer(charged, given):
    denoms = [500, 200, 100, 50, 20, 10, 5, 2, 1]

    if (change := (given - charged)) == 0:
        print("Exact")
        return

    print("Notes : ")
    for denom in denoms:
        num = change // denom
        print(f"{denom} : {num} ")
        change -= num * denom

        if denom == 10:
            print("Coins : ")


# changer(24, 500)


"""The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20,...,100."""

import enum
import random
from datetime import datetime


# Generate a random birthday in the format MM-DD
def generate_random_birthday():
    month = random.randint(1, 12)  # Month between 1 and 12
    day = random.randint(1, 28)  # Day between 1 and 28 (to avoid month-specific issues)

    # Construct the birthday
    birthday = f"{day:02d}-{month:02d}"

    return birthday


def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False


# Test using k test cases with n people (n birthdays)
def same_birthday_test(k, n):
    num_of_same_birthday = 0
    for i in range(k):  # out of 10000 iterations eg.

        birthdays = set()
        for i in range(n):  # generate n birthday
            birthday = generate_random_birthday()
            print(birthday)
            if birthday in birthdays:
                num_of_same_birthday += 1
                print(birthdays)
                break
            birthdays.add(birthday)
        print("-------")
    print(num_of_same_birthday / k)


# Generate and print a random birthday
# same_birthday_test(100000, 18)


"""P-1.36 Write a Python program that inputs a list of words, separated by white-
space, and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book"""

words = "wd1 wodssdrd2 wosdrd3 wordd4 wordsdsd5 worddd1 wossrd2 words4"
word_list = words.split(" ")

dict_words = {}
for word in word_list:
    if len(word) not in dict_words:
        dict_words[len(word)] = {word}
    else:
        dict_words[len(word)].add(word)

print(sorted(dict_words.items(), key=lambda x: x[0]))

tups = [(1, 2), (5, 3), (6, 8), (2, 1)]
print(sorted(tups, key=lambda x: x[1]))

# LAMDA
list1 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]

print(list(map(lambda x: (x[0], x[1] ** 2), list1)))

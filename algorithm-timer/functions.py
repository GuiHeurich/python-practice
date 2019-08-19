import random
from random import randrange

def last(list):
    return list[-1]

def reverse(list):
    reversed = []
    while True:
        reversed.append(list[-1])
        del list[-1]
        if len(list) == 0:
            break
    return reversed

def shuffle(list):
    shuffled = []
    while True:
        random_element = randrange(len(list))
        shuffled.append(list[random_element])
        list[random_element] = list[-1]
        list.pop()
        if len(list) == 0:
            break
    return shuffled

def find_duplicate(list):
    uniques = set(list)
    duplicates = []
    for x in list:
        if x not in duplicates:
            if x in uniques:
                duplicates.append(x)
    return duplicates

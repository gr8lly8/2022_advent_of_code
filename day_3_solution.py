#!/usr/bin/env python

priorities = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

sum_me = []

from itertools import islice

with open("day_3_input.txt", "r") as fin:
    lines = list(fin.readlines())
    for x in range(3, 303, 3):
        if x == 3:
            mini_list = lines[0:x]
            a = mini_list[0].strip()
            b = mini_list[1].strip()
            c = mini_list[2].strip()
            for item in set(a) & set(b) & set(c):
                sum_me.append(priorities[item])
        else:
            small = x - 3
            mini_list = lines[small:x]
            a = mini_list[0].strip()
            b = mini_list[1].strip()
            c = mini_list[2].strip()
            for item in set(a) & set(b) & set(c):
                sum_me.append(priorities[item])


#    for line in fin.readlines():
#        a, b = line[: len(line) // 2], line[len(line) // 2 :]
#        overlap = [value for value in a if value in b]
#        key = list(set(overlap))
#        for i in key:
#            sum_me.append(priorities[i])


print(sum(sum_me))

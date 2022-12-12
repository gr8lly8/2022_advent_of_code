#!/usr/bin/env python

with open("day_6_input.txt", "r") as fin:
    input_list = list(fin.read())
    start = 0
    finish = 14
    marker = input_list[start:finish]
    while len(marker) != len(set(marker)):
        start = start + 1
        finish = finish + 1
        marker = input_list[start:finish]
    else:
        print(finish)

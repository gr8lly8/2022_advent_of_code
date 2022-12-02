#!/usr/bin/env python
with open("day1_input.txt", "r") as fin:
    # elfs_calories = {}
    calories_list = []
    for index, elf in enumerate(fin.read().split("\n\n")):
        calories = []
        for i in elf.split("\n"):
            calories.append(int(i))
        #    key, value = index + 1, int(sum(calories))
        #    elfs_calories[key] = value
        calories_list.append(sum(calories))
    #    print(max(elfs_calories, key=elfs_calories.get))
    print(max(calories_list))
    calories_list.sort()
    print(sum(calories_list[-3:]))

#!/usr/bin/env python

dict = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

score_from_games = []
with open("day2_input.txt", "r") as fin:
    for line in fin.readlines():
        score_from_games.append(dict[line.strip()])

print(score_from_games)
print(sum(score_from_games))

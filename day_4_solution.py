#!/usr/bin/env python

total_overlap = []
# with open("test.txt", "r") as fin:
with open("day_4_input.txt", "r") as fin:
    lines = list(fin.readlines())
    for line in lines:
        elf_1 = line.split(",")[0]
        elf_2 = line.strip("\n").split(",")[-1]

        elf_1_range = range(int(elf_1.split("-")[0]), int(elf_1.split("-")[-1]) + 1)
        elf_2_range = range(int(elf_2.split("-")[0]), int(elf_2.split("-")[-1]) + 1)

        if len(elf_1_range) == 0:
            if (
                int(elf_2.split("-")[0])
                <= int(elf_1.split("-")[0])
                <= int(elf_2.split("-")[-1])
            ):
                total_overlap.append(line.strip("\n"))
        elif len(elf_2_range) == 0:
            if (
                int(elf_1.split("-")[0])
                <= int(elf_2.split("-")[0])
                <= int(elf_1.split("-")[-1])
            ):
                total_overlap.append(line.strip("\n"))
        elif list(set(elf_1_range) & set(elf_2_range)):
            #        elif set(elf_1_range).issubset(elf_2_range):
            total_overlap.append(line.strip("\n"))

#        elif set(elf_2_range).issubset(elf_1_range):
#            total_overlap.append(line.strip("\n"))

# print(total_overlap)
print(len(total_overlap))

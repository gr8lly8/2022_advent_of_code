#!/usr/bin/env python
import numpy as np
import pandas as pd

instructions = []
crates = []

# with open("test.txt", "r") as fin:
with open("day_5_input.txt", "r") as fin:
    lines = list(fin.readlines())
    for line in lines:
        if line.startswith("move"):
            instructions.append(line)
        else:
            line = line.replace("    ", " [] ")
            crates.append(line.split())


crates = [x for x in crates if x]
crates_df = pd.DataFrame(crates)
crates_df_T = crates_df.T
crates_df_T = crates_df_T[crates_df_T.columns[::-1]]
crates_df_T.drop(columns=crates_df_T.columns[0], axis=1, inplace=True)
crate_lists = crates_df_T.values.tolist()
new_crates_lists = []
for crates in crate_lists:
    if "[]" in crates:
        crates = list(filter(lambda a: a != "[]", crates))
        new_crates_lists.append(crates)
    else:
        new_crates_lists.append(crates)

for crates in new_crates_lists:
    crates.insert(0, "X")

for item in instructions:
#    print(new_crates_lists)
#    print(item)

    how_many = item.split(" ")[1]
    from_list = item.split(" ")[3]
    to_list = item.split(" ")[5].strip()

    new_crates_lists[int(to_list) - 1].extend(
        new_crates_lists[int(from_list) - 1][-int(how_many) :]
    )
    del new_crates_lists[int(from_list) - 1][-int(how_many) :]

#    print(new_crates_lists)

## part one
#    for x in range(0, int(how_many)):
#        new_crates_lists[int(to_list) - 1].append(
#            new_crates_lists[int(from_list) - 1][-1]
#        )
#        del new_crates_lists[int(from_list) - 1][-1]
#    print(new_crates_lists)

print([item[-1] for item in new_crates_lists])

"""
ID: wangyan27
LANG: PYTHON3
PROG: beads
"""


fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')

number_beads = int( fin.readline().strip() )
color_beads = [i for i in fin.readline().strip() ]


collection_numbers = []
for break_point in range(number_beads):
    color_bead_1 = color_beads[ break_point ]
    color_bead_2 = color_beads[ break_point - 1]

    broken_necklace = color_beads[break_point:] + color_beads[:break_point]

    collection_number = 0
    for i in broken_necklace:
        if i == color_bead_1 or i == "w":
            collection_number += 1
        elif i != color_bead_1 and color_bead_1 == "w":
            collection_number += 1
            color_bead_1 = i
        else:
            break
    for i in broken_necklace[::-1]:
        if i == color_bead_2 or i == "w":
            collection_number += 1
        elif i != color_bead_2 and color_bead_2 == "w":
            collection_number += 1
            color_bead_2 = i
        else:
            break

    collection_numbers.append(collection_number)

max_collection_number = min( [max(collection_numbers), number_beads] )

fout.write(str(max_collection_number) + '\n')
fout.close()
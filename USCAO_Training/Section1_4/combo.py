"""
ID: wangyan27
LANG: PYTHON3
PROG: combo
"""


fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')

N = int( fin.readline())

farmer_combin = list( map(int, fin.readline().split() ) )
master_combin = list( map(int, fin.readline().split() ) )

import itertools

count = 0
for d1, d2, d3 in itertools.product( range(1, N+1), repeat = 3):
    answer1, answer2 = True, True
    if  N-2 > abs( d1 - farmer_combin[0] )  > 2 or N-2 > abs( d2 - farmer_combin[1] ) > 2 or N-2 > abs( d3 - farmer_combin[2] ) > 2:
        answer1 = False

    if N-2 > abs( d1 - master_combin[0] ) > 2 or N-2 > abs( d2 - master_combin[1] ) > 2 or N-2 > abs( d3 - master_combin[2] ) > 2:
        answer2 = False
    
    if answer1 or answer2:
        count += 1

fout.write( str(count) + "\n")
fout.close()
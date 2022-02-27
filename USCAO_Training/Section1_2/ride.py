"""
ID: wangyan27
LANG: PYTHON3
PROG: ride
"""



with open('ride.in', 'r') as fin:
    comet1 = fin.readline().strip()
    comet2 = fin.readline().strip()
prod1, prod2 = 1, 1

print(comet1)
for c in comet1: prod1 *= ord(c) - ord('A') + 1
for c in comet2: prod2 *= ord(c) - ord('A') + 1


with open('ride.out', 'w') as fout:
    if prod1 % 47 == prod2 % 47: fout.write('GO\n')
    else: fout.write('STAY\n')

fout.close()
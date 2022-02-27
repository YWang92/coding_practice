"""
ID: wangyan27
LANG: PYTHON3
PROG: barn1
"""


fin = open ('barn1.in', 'r')
fout = open ('barn1.out', 'w')


M, S, C = map(int, fin.readline().split())

cows = list(map(int, fin.read()[:-1].split('\n')))
cows.sort()

if M >= C:
    result = C
else:
    gaps = [(cows[i+1] - cows[i] - 1 ) for i in range(C-1)]
    
    gaps.sort()
    print(gaps)

    mg = 0  # max gaps
    for i in range(M-1):
        mg += gaps.pop()

    result = max(cows) - min(cows) + 1 - mg


fout.write(str(result) + '\n')


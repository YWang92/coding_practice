"""
ID: wangyan27
LANG: PYTHON3
PROG: milk
"""


fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')


[N, M] =  [int(_) for _ in fin.readline().split()]


each_farmer = []
for _ in range(M):
    each_farmer.append( [int(_) for _ in fin.readline().split()] )
    each_farmer.sort()

expense, milk = 0, 0

for farmer in each_farmer:
    price, production = farmer[0], farmer[1]
    
    if milk + production <= N:
        expense += price * production
    else:
        production = N - milk
        expense += price * production
    
    milk += production


fout.write(str(expense)+ '\n')
fout.close()

"""
ID: wangyan27
LANG: PYTHON3
PROG: palsquare
"""


fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')


base = int( fin.readline().strip() )

def base_switch(number, base):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A','B','C','D','E','F', "G", "H", "I", "J"]

    num_new_base = ""
    while True:
        residual = number // base
        bit = number % base
        
        num_new_base += digits[bit]
        number = residual
        
        if residual == 0:
            break
    return num_new_base[::-1]

for i in range(1, 301):
    isquare = i**2
    isquare = base_switch(isquare, base)

    if isquare == isquare[::-1]:
        fout.write(base_switch(i, base) + " " + isquare + '\n')
fout.close()
    
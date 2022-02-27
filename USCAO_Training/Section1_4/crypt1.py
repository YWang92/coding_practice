"""
ID: wangyan27
LANG: PYTHON3
PROG: crypt1
"""

import itertools

fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')

N = int( fin.readline().split()[0] )

digits = list( map(int, fin.readline().split()) )

def in_digits(number):
    number = [int(_) for _ in str(number)]
    for d in number:
        if d not in digits:
            return False

    return True


num_solution = 0
for d1, d2, d3, d4, d5 in itertools.product(digits, repeat = 5):
    number1 = d1 + d2 * 10 + d3 * 100
    partial1 = number1 * d4
    partial2 = number1 * d5

    if len(str(partial1)) == 3 and in_digits(partial1):
        if len(str(partial2)) == 3 and in_digits(partial2):
            product = partial1 + partial2 * 10
    
            if in_digits(product):
                num_solution += 1
            

fout.write(str(num_solution)+ '\n')
fout.close()
"""
ID: wangyan27
LANG: PYTHON3
PROG: dualpal
"""


fin = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')



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

def determine_dual_pal(number, base):

    num_new_base = base_switch(number, base)
    if num_new_base == num_new_base[::-1]:
        return number, 1
    else:
        return number, 0




[N, S] =  [int(_) for _ in fin.readline().split()]

dual_palindromes = []
number = S + 1
while True:
    count = 0
    for base in range(2, 11):
        [i, j] = determine_dual_pal(number, base)
        count += j

        if count >= 2:
            dual_palindromes.append(i)
            break
    
    if len(dual_palindromes) == N:
        break

    number += 1

dual_palindromes

            

for dual_pal in dual_palindromes:    
    fout.write(str(dual_pal)+ '\n')
fout.close()
#Uses python3

import sys


def lcs3(a, b, c):
    len_a = len(a) + 1  # first index
    len_b = len(b) + 1  # second index
    len_c = len(c) + 1  # third index
    
    T = [[[0 for _ in range(len_c)] for _ in range(len_b)] for _ in range(len_a)]
    
    for i in range(1, len_a):
        for j in range(1, len_b):
            for k in range(1, len_c):
                if a[i-1] == b[j-1] == c[k-1]:
                    T[i][j][k] = T[i-1][j-1][k-1] + 1
                else:
                    T[i][j][k] = max(T[i-1][j][k], T[i][j-1][k], T[i][j][k-1])

    return T[len(a)][len(b)][len(c)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    an = data[0]
    data = data[1:]
    a = data[:an]

    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]

    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]

    print(lcs3(a, b, c))

# cat data.txt | python3 lcs3.py
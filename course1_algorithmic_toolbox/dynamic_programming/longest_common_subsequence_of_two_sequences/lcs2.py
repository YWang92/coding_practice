#Uses python3

import sys

def lcs2(a, b):
    len_a = len(a) + 1  # first index
    len_b = len(b) + 1  # second index
    T = [[0 for _ in range(len_b)] for _ in range(len_a)]
    
    for i in range(1, len_a):
        for j in range(1, len_b):
            T[i][j] = max([max(sub_T[:j]) for sub_T in T[:i]])
            if a[i-1] == b[j-1]:
                T[i][j] += 1
            
    return max([max(_) for _ in T])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

# cat data.txt | python3 lcs2.py
# Uses python3
def edit_distance(s, t):
    len_s = len(s) + 1  # first index
    len_t = len(t) + 1  # second index
    T = [[0 for _ in range(len_t)] for _ in range(len_s)]
    for i in range(1, len_s):
        T[i][0] = i
    for j in range(1, len_t):
        T[0][j] = j

    for i in range(1, len_s):
        for j in range(1, len_t):
            x, y, z = T[i][j-1]+1, T[i-1][j]+1, T[i-1][j-1]
            if s[i-1] != t[j-1]:
                z += 1
            T[i][j] = min(x, y, z)


    return T[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))

# cat data.txt | python3 edit_distance.py
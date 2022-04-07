# Uses python3
import sys
denoms = [1, 3, 4]

def get_change(m):
    T = [0]
    for i in range(1, m+1):
        solutions = []
        for denom in denoms:
            if denom <= i:
                solutions.append(T[i-denom])
        solution = min(solutions) + 1
        T.append(solution)

    return T[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

# cat data.txt | python3 change_dp.py 
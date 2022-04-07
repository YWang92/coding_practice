# Uses python3
from logging import lastResort
import sys
from collections import namedtuple

Solution = namedtuple("solution", ["value", "bars"])


def optimal_weight(W, w):
    T = [Solution(0, [])]

    for total_weight in range(1, W+1):
        solution_list = []
        for bar in range(len(w)):
            rest_weight = total_weight - w[bar]
            if rest_weight < 0:
                solution_list.append(Solution(0, []))
            else:
                for i in reversed(range(rest_weight+1)):
                    if bar not in T[i].bars:
                        solution = Solution(T[i].value + w[bar], T[i].bars + [bar])
                        solution_list.append(solution)
                        break
            
        T.append(max(solution_list, key=lambda x:x.value))

    return T[-1].value


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

# cat data.txt | python3 knapsack.py
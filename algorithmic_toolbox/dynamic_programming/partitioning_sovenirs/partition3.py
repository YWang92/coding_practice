# Uses python3
import sys
import itertools
from collections import namedtuple

Solution = namedtuple("solution", ["value", "souvenirs"])


def partition3(A):
    if len(A) < 3 or sum(A) % 3 != 0:
        return 0
    T = [Solution(0, [])]

    summation, partition = sum(A), int(sum(A)/3)
    for total_value in range(1, sum(A)+1):
        solution_list = []
        for souvenir in range(len(A)):
            rest_value = total_value - A[souvenir]
            if rest_value < 0:
                solution_list.append(Solution(0, []))
            else:
                for i in reversed(range(rest_value+1)):
                    if souvenir not in T[i].souvenirs:
                        solution = Solution(T[i].value + A[souvenir], T[i].souvenirs + [souvenir])
                        solution_list.append(solution)
        optimal_solution = max(solution_list, key=lambda x:x.value)
        if total_value == partition and optimal_solution.value != partition:
            return 0
        else:
            T.append(optimal_solution)

    return 1



def test():
    pass


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))


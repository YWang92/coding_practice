#Uses python3

import sys


def acyclic(adj):
    n = len(adj)
    vertices, visited = list(range(n)), []
    for v in vertices:
        if v not in visited:
            path = [v]
            while path:
                curr_v = path[-1]
                if len(adj[curr_v]) == 0:
                    visited.append(curr_v)
                    path.pop()
                else:
                    next_v = adj[curr_v].pop()
                    if next_v in path:
                        return 1
                    path.append(next_v)
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

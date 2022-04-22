#Uses python3

import sys


def dfs(adj, used, order, v):
    # write your code here
    to_explore = [v]
    while to_explore:
        curr_v = to_explore[-1]
        if len(adj[curr_v]) == 0:
            if used[curr_v] == 0:
                used[curr_v] = 1
                order.insert(0, curr_v)
            to_explore.pop()
        else:
            next_v = adj[curr_v].pop()
            to_explore.append(next_v)

    return adj, used, order


def toposort(adj):
    used = [0] * len(adj)
    order = []
    # write your code here
    for v in range(len(adj)):
        if used[v] != 0:
            pass
        else:
            adj, used, order = dfs(adj, used, order, v)
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

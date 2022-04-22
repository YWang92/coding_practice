#Uses python3

import sys

sys.setrecursionlimit(200000)


def dfs(adj, post_order, used, v):
    used[v] = 1
    for next_v in adj[v]:
        if used[next_v] == 0:
            dfs(adj, post_order, used, next_v)
    post_order.insert(0, v)


def number_of_strongly_connected_components(adj):
    result = 0
    used, post_order = [0] * len(adj), []
    adj_r = [[] for _ in range(len(adj))]

    for i in range(len(adj)):
        for j in adj[i]:
            adj_r[j].append(i)

    for v in range(len(adj)):
        if v not in post_order:
            dfs(adj, post_order, used, v)

    used = [0] * len(adj)
    for v in post_order:
        if used[v] == 0:
            result += 1
            dfs(adj_r, [], used, v)

    return result





if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))

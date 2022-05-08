#Uses python3

import sys


def negative_cycle(adj, cost):
    dist_max = 0
    for v1 in range(len(adj)):
        for v2_index, v2 in enumerate(adj[v1]):
            dist_max = abs(cost[v1][v2_index])

    dists = [dist_max] * len(adj)
    s, dists[0] = 0, 0
    for iteration in range(len(adj)):
        for v1 in range(len(adj)):
            for v2_index, v2 in enumerate(adj[v1]):
                if dists[v2] > dists[v1] + cost[v1][v2_index]:
                    dists[v2] = dists[v1] + cost[v1][v2_index]
                    if iteration == len(adj) - 1:
                        return 1
    return 0




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))

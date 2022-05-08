#Uses python3

import sys
import queue
import math


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # determine whether a vertex is reachable
    to_explore, reachable[s] = [s], 1
    while to_explore:
        v1 = to_explore.pop()
        for v2 in adj[v1]:
            if reachable[v2] == 0:
                reachable[v2] = 1
                to_explore.append(v2)

    distance[s], prev = 0, [-1] * len(adj)
    to_explore = []
    for iteration in range(len(adj)):
        for v1 in range(len(adj)):
            for v2_index, v2 in enumerate(adj[v1]):
                if reachable[v1] != 0 and reachable[v2] != 0:
                    if distance[v2] > distance[v1] + cost[v1][v2_index]:
                        distance[v2] = distance[v1] + cost[v1][v2_index]
                        prev[v2] = v1
                        if iteration == len(adj) - 1:
                            shortest[v2] = 0
                            to_explore.append(v2)
    visited = []
    while to_explore:
        v1 = to_explore.pop()
        visited.append(v1)
        for v2 in adj[v1]:
            shortest[v2] = 0
            if v2 not in visited and v2 not in to_explore:
                to_explore.append(v2)


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

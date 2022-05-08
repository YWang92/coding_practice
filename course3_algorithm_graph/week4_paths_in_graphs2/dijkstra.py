#Uses python3

import sys
import queue
import heapq

def distance(adj, cost, s, t):
    dists, prev = [-1] * len(adj), [-1] * len(adj)
    dists[s] = 0
    to_explore = []
    heapq.heappush(to_explore, [dists[s], s])

    while to_explore:
        curr_v = heapq.heappop(to_explore)[1]
        for i, next_v in enumerate(adj[curr_v]):
            weight = cost[curr_v][i]
            if dists[next_v] == -1 or dists[next_v] > dists[curr_v] + weight:
                dists[next_v] = dists[curr_v] + weight
                prev[next_v] = curr_v
                heapq.heappush(to_explore, [dists[next_v], next_v])

    return dists[t]


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
    s, t = data[0] - 1, data[1] - 1

    print(distance(adj, cost, s, t))

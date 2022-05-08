#Uses python3

import sys
import queue

def distance(adj, s, t):
    to_explore = queue.Queue()
    distances = [-1] * len(adj)
    to_explore.put(s)
    distances[s] = 0
    while not to_explore.empty():
        curr_v = to_explore.get()
        for next_v in adj[curr_v]:
            if distances[next_v] == -1:
                distances[next_v] = distances[curr_v] + 1
                to_explore.put(next_v)

    return distances[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))

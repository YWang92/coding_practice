#Uses python3

import sys
import queue

def bipartite(adj):
    colors = [0] * len(adj)
    for start in range(len(adj)):
        if colors[start] == 0:
            colors[start] = 1
            to_explore = queue.Queue()
            to_explore.put(start)

            while not to_explore.empty():
                curr_v = to_explore.get()
                for next_v in adj[curr_v]:
                    if colors[next_v] == 0:
                        colors[next_v] = colors[curr_v] * (-1)
                        to_explore.put(next_v)
                    elif colors[next_v] == colors[curr_v]:
                        return 0
    return 1


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
    print(bipartite(adj))

#Uses python3

import sys

def reach(adj, x, y):
    visited = []
    to_explore = [x]
    while to_explore:
        curr = to_explore.pop()
        visited.append(curr)
        neighbors = adj[curr]
        for neighbor in neighbors:
            if neighbor not in visited:
                to_explore.append(neighbor)
    if y in visited:
        return 1
    else:
        return 0


def number_of_components(adj):
    result = 0
    visited = []
    for vertex in range(len(adj)):
        to_explore = [vertex]
        if vertex not in visited:
            while to_explore:
                curr = to_explore.pop()
                visited.append(curr)
                neighbors = adj[curr]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        to_explore.append(neighbor)
            result += 1

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
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))

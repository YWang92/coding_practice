# python3
import numpy as np

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    n = len(data) # size of the binary heap
    for i in reversed(range(n)):
        parent_id = i
    
        while 2*parent_id + 1 <= n - 1:
            lchild_id, rchild_id = 2*parent_id + 1, 2*parent_id + 2

            if rchild_id > n - 1:
                if data[parent_id] > data[lchild_id]:
                    data[parent_id], data[lchild_id] = data[lchild_id], data[parent_id]
                    swaps.append([parent_id, lchild_id])
                    parent_id = lchild_id
                else:
                    break
            else:
                if data[parent_id] > data[lchild_id]:
                    if data[lchild_id] > data[rchild_id]:
                        data[parent_id], data[rchild_id] = data[rchild_id], data[parent_id]
                        swaps.append([parent_id, rchild_id])
                        parent_id = rchild_id
                    else:
                        data[parent_id], data[lchild_id] = data[lchild_id], data[parent_id]
                        swaps.append([parent_id, lchild_id])
                        parent_id = lchild_id
                elif data[parent_id] > data[rchild_id]:
                    data[parent_id], data[rchild_id] = data[rchild_id], data[parent_id]
                    swaps.append([parent_id, rchild_id])
                    parent_id = rchild_id
                else:
                    break
            
    return swaps
        


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

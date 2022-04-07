# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrderTranvers(self, node):
        result = []
        if self.left[node] != -1:
            result += self.inOrderTranvers(self.left[node])
        result.append(self.key[node])
        if self.right[node] != -1:
            result += self.inOrderTranvers(self.right[node])
        return result

    def inOrder(self):
        return self.inOrderTranvers(node=0)

    def preOrderTranvers(self, node):
        result = [self.key[node]]
        if self.left[node] != -1:
            result += self.preOrderTranvers(self.left[node])
        if self.right[node] != -1:
            result += self.preOrderTranvers(self.right[node])
        return result

    def preOrder(self):
        return self.preOrderTranvers(node=0)

    def postOrderTranvers(self, node):
        result = []
        if self.left[node] != -1:
            result += self.postOrderTranvers(self.left[node])
        if self.right[node] != -1:
            result += self.postOrderTranvers(self.right[node])
        result.append(self.key[node])
        return result

    def postOrder(self):
        return self.postOrderTranvers(node=0)


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()

# cat data.txt|python3 tree_order_slow.py

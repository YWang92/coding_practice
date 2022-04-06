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

    def inOrder(self):
        left, right = self.left.copy(), self.right.copy()
        key_stack = [0]
        result = []
        while key_stack:
            node_key = key_stack[-1]
            if left[node_key] == -1:
                result.append(self.key[node_key])
                key_stack.pop()
                if right[node_key] != -1:
                    key_stack.append(right[node_key])
                    right[node_key] = -1
            else:
                key_stack.append(left[node_key])
                left[node_key] = -1

        return result

    def preOrder(self):
        left, right = self.left.copy(), self.right.copy()
        key_stack = [0]
        result = []
        while key_stack:
            node_key = key_stack.pop()
            result.append(self.key[node_key])
            if self.right[node_key] != -1:
                key_stack.append(self.right[node_key])
            if self.left[node_key] != -1:
                key_stack.append(self.left[node_key])
        return result


    def postOrder(self):
        left, right = self.left.copy(), self.right.copy()
        key_stack = [0]
        result = []
        while key_stack:
            node_key = key_stack[-1]
            if left[node_key] == -1:
                if right[node_key] == -1:
                    result.append(self.key[node_key])
                    key_stack.pop()
                else:
                    key_stack.append(right[node_key])
                    right[node_key] = -1
            else:
                key_stack.append(left[node_key])
                left[node_key] = -1

        return result




def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()

# cat data.txt|python3 tree_order_slow.py

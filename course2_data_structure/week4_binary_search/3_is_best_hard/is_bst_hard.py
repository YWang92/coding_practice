#!/usr/bin/python3

import sys, threading
from collections import namedtuple

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size

Node = namedtuple('Node', ['key', 'left', 'right'])

def inOrder(tree):
    tree = [Node(node[0], node[1], node[2]) for node in tree]
    stack, result = [], []
    curr = 0
    while stack or curr != -1:
        if curr != -1:
            root = tree[curr]
            stack.append(root)
            curr = root.left
            if len(stack) >= 2 and root.key >= stack[-2].key:
                return False
        else:
            root = stack.pop()
            result.append(root.key)
            curr = root.right
    return result

def IsBinarySearchTree(tree):
    if not tree:
        return True
    in_order_list = inOrder(tree)
    if in_order_list:
        for i in range(len(in_order_list)-1):
            if in_order_list[i] > in_order_list[i+1]:
                return False
        return True
    else:
        return False


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
      tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
      print("CORRECT")
    else:
      print("INCORRECT")

threading.Thread(target=main).start()

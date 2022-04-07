# !/usr/bin/python3

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
        else:
            root = stack.pop()
            result.append(root.key)
            curr = root.right
    return result

def IsBinarySearchTree(tree):
    if not tree:
        return True
    in_order_list = inOrder(tree)
    for i in range(len(in_order_list)-1):
        if in_order_list[i] >= in_order_list[i+1]:
            return False
    return True


# def IsBinarySearchTree(tree):
#     if not tree:
#         return True
#     tree = [Node(node[0], node[1], node[2]) for node in tree]
#     index_stack = [0]
#     while index_stack:
#         node = tree[index_stack[-1]]
#         if node.right != -1:
#             right_child = tree[node.right]
#             if right_child.key <= node.key:
#                 return False
#             else:
#                 index_stack[-1] = node.right
#         if node.left != -1:
#             left_child = tree[node.left]
#             if left_child.key >= node.key:
#                 return False
#             else:
#                 index_stack.append(node.left)
#         if node.left == node.right == -1:
#             index_stack.pop()
#
#     return True


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


# cat data.txt|python3 is_bst.py

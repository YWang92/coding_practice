# python3

from ast import While
from asyncio import QueueEmpty
import queue
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
from collections import namedtuple

Vertex = namedtuple("Vertex", ['index', 'children'])

class TreeHeight:
    def read(self, input = []):
        if not input:
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))
        else:
            self.n = int( input[0] )
            self.parent = list(map(int, input[1].split() ))

    def tree_building(self):
        tree = [ Vertex( _ , [])  for _ in range(self.n)]

        for node_index in range(self.n):
            parent_index = self.parent[node_index]
            if parent_index != -1:
                tree[parent_index].children.append(node_index)
            else:
                root_index = node_index
                        
        return tree, root_index

    def compute_height(self):
        tree, root_index = self.tree_building()

        queue_1, queue_2 = [], []

        queue_1 += tree[root_index].children

        if queue_1:
                height = 2
        else:
                height = 1
                return height

        while True:
            if len(queue_1) != 0 or len(queue_2) != 0:

                if len(queue_1) != 0:
                    queue_2 += tree[ queue_1[-1] ].children
                    queue_1.pop()

                else:
                    queue_1, queue_2 = queue_2, queue_1
                    height += 1

            else:
                return height

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
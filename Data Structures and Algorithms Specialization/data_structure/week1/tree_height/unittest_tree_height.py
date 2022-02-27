import unittest
from tree_height import TreeHeight

def height_of_tree(input):
    tree = TreeHeight()
    tree.read(input)
    return tree.compute_height()

input, solution = ['1000', '-1 ' + '0 '*997 + '1 ' + '998 '], 4
print( height_of_tree(input), solution)


class TestNameGetter(unittest.TestCase):

    def test_small(self):
        input, solution = ['1', '-1'], 1
        self.assertEqual( height_of_tree(input), solution)

        input, solution = ['10', '-1 0 0 0 0 0 0 0 0 0'], 2
        self.assertEqual( height_of_tree(input), solution
        
        input, solution = ['1000', '-1 ' + '0 '*998 + '1 '], 3
        self.assertEqual( height_of_tree(input), solution
        
        input, solution = ['1000', '-1 ' + '0 '*997 + '1 ' + '998 '], 4
        self.assertEqual( height_of_tree(input), solution


        
if __name__ == '__main__':
    unittest.main()





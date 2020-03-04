import unittest
from main import Tree

root = Tree(5)
root.insert(3, right=False)
root.left.insert(2, right=False)
root.left.insert(5)
root.insert(7)
root.right.insert(0)
root.right.insert(1, right=False)
root.right.right.insert(2, right=False)
root.right.right.insert(8)
root.right.right.right.insert(5)

print ('Sum of the tree elements = ', root.sum())
print ('Mean of the tree elements = ', root.mean())
print ('Median of the tree elements = ', root.median())


class TestTree(unittest.TestCase):

    def test_sum(self):
        self.assertAlmostEqual(Tree.sum(root), 38)
        self.assertAlmostEqual(Tree.sum(root.left), 10)
        self.assertAlmostEqual(Tree.sum(root.right), 23)
        self.assertAlmostEqual(Tree.sum(root.left.left), 2)

    def test_mean(self):
        self.assertAlmostEqual(Tree.mean(root), 3.8)
        self.assertAlmostEqual(Tree.mean(root.left), 10 / 3)
        self.assertAlmostEqual(Tree.mean(root.right.left), 1)
        self.assertAlmostEqual(Tree.mean(root.right.right), 3.75)

    def test_median(self):
        self.assertAlmostEqual(Tree.median(root), 4.0)
        self.assertAlmostEqual(Tree.median(root.right), 3.5)
        self.assertAlmostEqual(Tree.median(root.left), 3.0)
        self.assertAlmostEqual(Tree.median(root.left.right), 5.0)

    def test_types(self):
        self.assertRaises(TypeError, Tree.insert, '23')
        self.assertRaises(TypeError, Tree.insert, 2 + 3j)
        self.assertRaises(TypeError, Tree.insert, 2.2)
        self.assertRaises(TypeError, Tree.insert, [2])
        self.assertRaises(TypeError, Tree.insert, [2], right=1)
        self.assertRaises(TypeError, Tree.insert, [2], right=-1)
        self.assertRaises(TypeError, Tree.insert, [2], right='s')


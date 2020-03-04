
class Tree:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val, right=True):
        if type(val) is not int:
            raise TypeError('Value should be an integer.')
        if type(right) is not bool:
            raise TypeError('Optional parameter should be a boolean.')
        if self.val is not None:
            if right:
                if self.right is None:
                    self.right = Tree(val)
                else:
                    self.right.insert(val)
            else:
                if self.left is None:
                    self.left = Tree(val)
                else:
                    self.left.insert(val)
        else:
            self.val = val

    def sum(self):
        res = 0
        if self.left is not None:
            res += self.left.sum()
        if self.val is not None:
            res += self.val
        if self.right is not None:
            res += self.right.sum()
        return res

    def count(self):
        res = 0
        if self.left is not None:
            res += self.left.count()
        if self.val is not None:
            res += 1
        if self.right is not None:
            res += self.right.count()
        return res

    def mean(self):
        return float(self.sum()) / self.count()

    def treeToList(self):
        lst = []
        current_level = [self]
        while current_level:
            for child in current_level:
                lst.append(child.val)
            children = list()
            for n in current_level:
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)
            current_level = children
        return lst

    def median(self):
        sortedLst = sorted(self.treeToList())
        index = (len(sortedLst) - 1) // 2
        if len(sortedLst) % 2:
            return sortedLst[index]
        else:
            return (sortedLst[index] + sortedLst[index + 1]) / 2.0


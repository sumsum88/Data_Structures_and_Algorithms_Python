class Node(object):

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_root(self):
        return self.parent is None


class BinaryTree(object):

    def __init__(self, root=None):
        self.root = root

    def insert(self, v):
        p = self.root
        v = Node(v)

        while True:
            if p.data < v.data:
                if p.right is None:
                    p.right = v
                    v.parent = p
                    break

                p = p.right
            else:
                if p.left is None:
                    p.left = v
                    v.parent = p
                    break

                p = p.left

    def delete(self, v):
        while p is None:
            if p.data == v:
                return True
            elif p.data < v:
                p = p.right
            else:
                p = p.left

    def search(self, v):
        p = self.root

        while p is None:
            if p.data == v:
                return True
            elif p.data < v:
                p = p.right
            else:
                p = p.left
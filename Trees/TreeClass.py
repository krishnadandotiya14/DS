
class BinaryTree:
    def __init__(self,value):
        self.root = value
        self.left = None
        self.right = None

    def getLeftChild(self):
        return self.root.left

    def getRightChild(self):
        return self.root.right

    def getCurrentVal(self):
        return self.root

from TreeClass import BinaryTree
import sys

def max_in_binarytree(root):
    if root is None:
        return -sys.maxsize
    curr = root.getCurrentVal()
    left = max_in_binarytree(root.left)
    right = max_in_binarytree(root.right)
    return max(curr, left, right)


def min_in_binarytree(root):
    if root is None:
        return sys.maxsize
    curr = root.getCurrentVal()
    left = min_in_binarytree(root.left)
    right = min_in_binarytree(root.right)
    return min(curr, left, right)


# Create Tree
t = BinaryTree(1)
t.left = BinaryTree(2)
t.right = BinaryTree(3)
t.left.left = BinaryTree(4)
t.left.right = BinaryTree(5)
t.right.left = BinaryTree(6)
t.right.right = BinaryTree(7)
# t.left.left.left = BinaryTree(8)

print("Max in tree: ", max_in_binarytree(t))
print("Min in tree: ", min_in_binarytree(t))


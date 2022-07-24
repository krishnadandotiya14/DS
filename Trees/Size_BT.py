from TreeClass import BinaryTree

def size_binarytree(root):
    if root is None:
        return 0
    return size_binarytree(root.left) + size_binarytree(root.right) + 1

# Create Tree
t = BinaryTree(1)
t.left = BinaryTree(2)
t.right = BinaryTree(3)
t.left.left = BinaryTree(4)
t.left.right = BinaryTree(5)
t.right.left = BinaryTree(6)
t.right.right = BinaryTree(7)
t.left.left.left = BinaryTree(8)

print("Size of tree: ", size_binarytree(t))
from TreeClass import BinaryTree

def height_bt(root):
    if root is None:
        return 0
    # Get left and right part of Tree
    left = height_bt(root.left)
    right = height_bt(root.right)
    # Take the part which is big and all 1 for current level
    return max(left,right) + 1

# Create Tree
t = BinaryTree(1)
t.left = BinaryTree(2)
t.right = BinaryTree(3)
t.left.left = BinaryTree(4)
t.left.right = BinaryTree(5)
t.right.left = BinaryTree(6)
t.right.right = BinaryTree(7)
t.left.left.left = BinaryTree(8)


print("height of tree: ",height_bt(t))
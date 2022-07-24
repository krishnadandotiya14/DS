from TreeClass import BinaryTree

def inorder_traverse(root):
    if root == None:
        return
    inorder_traverse(root.left)
    print(root.getCurrentVal(),end=" ")
    inorder_traverse(root.right)

def preorder_traverse(root):
    if root == None:
        return
    print(root.getCurrentVal(),end=" ")
    preorder_traverse(root.left)
    preorder_traverse(root.right)

def postorder_traverse(root):
    if root == None:
        return
    postorder_traverse(root.left)
    postorder_traverse(root.right)
    print(root.getCurrentVal(),end=" ")


# Create Tree
t = BinaryTree(1)
t.left = BinaryTree(2)
t.right = BinaryTree(3)
t.left.left = BinaryTree(4)
t.left.right = BinaryTree(5)
t.right.left = BinaryTree(6)
t.right.right = BinaryTree(7)


inorder_traverse(t)
print('\n===')
preorder_traverse(t)
print('\n===')
postorder_traverse(t)
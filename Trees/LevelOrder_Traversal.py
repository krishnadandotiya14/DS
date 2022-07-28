import queue
from TreeClass import BinaryTree


def levelorder_traversal(tree):
    ans = []
    if tree == None:
        return
    q = queue.Queue()
    q.put(tree)
    node = None

    while not q.empty():
        node = q.get()
        ans.append(node.root)

        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

    return ans


# Create Tree  !!!
t = BinaryTree(1)
t.left = BinaryTree(2)
t.right = BinaryTree(3)
t.left.left = BinaryTree(4)
t.left.right = BinaryTree(5)
t.right.left = BinaryTree(6)
t.right.right = BinaryTree(7)
t.left.left.left = BinaryTree(8)

# Calling !!!!
print(levelorder_traversal(t))


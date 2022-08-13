from TreeClass import BinaryTree

def iter_preorder(head):
    stack = []
    if head is None:
        return head
    curr = head
    stack.append(curr)
    while len(stack):
        if stack.left
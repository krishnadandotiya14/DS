from SinglyLinkedLIst import SLLNode
from Insert import print_ll


def palindrome_ll(head):

    if head is None or head.next is None:
        return True

    # Find Middle
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    middle = slow

    # Reverse after middle
    head2 = None
    curr = middle.next
    prev = None
    while curr.next:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    if curr:
        head2 = curr
        curr.next = prev

    # Now match value on two half of linkedlist
    while head2:
        if head.value != head2.value:
            return False
        head = head.next
        head2 = head2.next
    return True


if __name__ == "__main__":
    # Create Singly LinkedList
    A = SLLNode(1)
    B = SLLNode(2)
    C = SLLNode(3)
    D = SLLNode(2)
    E = SLLNode(1)
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    head = A

    print_ll(head)
    print(" ")
    print("A Palindrome LinkedLIst:: ?? ")
    print(palindrome_ll(head))
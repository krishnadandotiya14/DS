from SinglyLinkedLIst import SLLNode
from Insert import print_ll


def reverse_ll(head):

    if head is None or head.next is None:
        return head
    curr = head
    prev = None
    while curr.next is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    if curr:
        head = curr
        curr.next = prev
    return head


if __name__ == "__main__":
    # Create Singly LinkedList
    A = SLLNode(11)
    B = SLLNode(23)
    C = SLLNode(35)
    D = SLLNode(48)
    E = SLLNode(57)
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    head = A

    print_ll(head)
    print(" ")
    print("Reverse of a LinkedLIst::")
    print_ll(reverse_ll(head))

from SinglyLinkedLIst import SLLNode
from Insert import print_ll

def middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.value


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
    print("Middle of LinkedLIst::", middle(head))
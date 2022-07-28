from SinglyLinkedLIst import SLLNode
from Insert import print_ll


def delete_n_last_ll(head,n):

    if head is None:
        return False

    ptr = head
    loc = head
    count = 0
    while ptr.next:
        if count < n:
            count += 1
            ptr = ptr.next
        else:
            loc = loc.next
            ptr = ptr.next

    loc.next = loc.next.next
    return head


if __name__ == "__main__":
    # Create Singly LinkedList
    A = SLLNode(1)
    B = SLLNode(2)
    C = SLLNode(3)
    D = SLLNode(4)
    E = SLLNode(5)
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    head = A

    print_ll(head)
    print(" ")
    n = 3
    print("Remove ",str(n),"th element from last in LinkedLIst::--> ")
    t = delete_n_last_ll(head,n)
    print_ll(t)
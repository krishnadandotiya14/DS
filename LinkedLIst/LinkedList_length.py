from SinglyLinkedLIst import SLLNode
from Insert import print_ll

def length_ll(head):
    count = 0
    if head is None:
        return count
    while head:
        count += 1
        head = head.next
    return count


if __name__ == "__main__":

    # Create Singly LinkedList
    A = SLLNode(11)
    B = SLLNode(23)
    C = SLLNode(35)
    D = SLLNode(48)
    A.next = B
    B.next = C
    C.next = D
    head = A

    print_ll(head)
    print(" ")
    print("Length of LinkedLIst::",length_ll(head))
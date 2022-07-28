from SinglyLinkedLIst import SLLNode

def print_ll(head):
    curr = head
    while curr:
        print(curr.value,end=" -> ")
        curr = curr.next

def insert_at_end(head,value):
    node = SLLNode(value)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = node
    print_ll(head)

def insert_at_start(head,value):
    node = SLLNode(value)
    node.next = head
    head = node
    print_ll(head)

def insert_in_between(head,after,value):
    node = SLLNode(value)
    curr = head
    while curr:
        if curr.value == after:
            temp = curr.next
            curr.next = node
            node.next = temp
        curr = curr.next
    print_ll(head)

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
    #print_ll(head)

    # CHeck Insert Functions
    insert_at_start(head, 6)     # 6 -> 11 -> 23 -> 35 -> 48 ->
    print(" ")
    insert_at_end(head, 100)     # 11 -> 23 -> 35 -> 48 -> 100 ->
    print(" ")
    insert_in_between(head,35,40)   # 11 -> 23 -> 35 -> 40 -> 48 -> 100 ->


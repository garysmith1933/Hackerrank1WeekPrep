def mergeLists(head1, head2):
    dummyHead = SinglyLinkedList()
    tail = dummyHead
    
    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
            
        else:
            tail.next = head2
            head2 = head2.next
        
        tail = tail.next
    
    if not head1:
        tail.next = head2
    
    else:
        tail.next = head1
    
    return dummyHead.next
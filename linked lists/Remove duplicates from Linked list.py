# 9. remove duplicate elements from linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeDuplicates(head):

    current = head

    while current and current.next:

        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head

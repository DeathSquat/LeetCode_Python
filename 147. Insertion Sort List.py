# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)  # Dummy node to simplify insertion
        dummy.next = head
        curr = head.next
        head.next = None  # Separate the first node from the unsorted part

        while curr:
            prev = dummy  # Start at the beginning of the sorted part
            next_node = curr.next  # Save the next node

            # Find the correct position to insert `curr`
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert `curr` between `prev` and `prev.next`
            curr.next = prev.next
            prev.next = curr

            # Move to the next node in the original list
            curr = next_node

        return dummy.next  # The sorted linked list starts after dummy

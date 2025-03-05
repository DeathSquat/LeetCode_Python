# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        
        # Step 1: Detect cycle using slow and fast pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Cycle detected
                break
        else:
            return None  # No cycle
        
        # Step 2: Find the cycle start node
        slow = head  # Reset slow to head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow  # The node where the cycle begins

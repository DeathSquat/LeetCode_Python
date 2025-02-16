# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
 
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        # Helper function to find the middle node and split the list
        def findMiddle(left, right):
            slow = left
            fast = left
            prev = None
            while fast != right and fast.next != right:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            # Disconnect left half from the middle
            if prev:
                prev.next = None
            return slow
        
        mid = findMiddle(head, None)
        root = TreeNode(mid.val)
        
        # Recursively build left and right subtrees
        if mid != head:  # To avoid infinite recursion
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root

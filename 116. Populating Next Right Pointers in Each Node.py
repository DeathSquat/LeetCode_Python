"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        leftmost = root  # Start from the root of the tree
        
        while leftmost.left:  # Since it's a perfect tree, we check left child existence
            current = leftmost  # Traverse nodes at the current level
            
            while current:
                # Connect left child to right child
                current.left.next = current.right
                
                # Connect right child to the left child of the next node (if exists)
                if current.next:
                    current.right.next = current.next.left
                
                # Move to the next node in the same level
                current = current.next
            
            # Move to the next level
            leftmost = leftmost.left
        
        return root

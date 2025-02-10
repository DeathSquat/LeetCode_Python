# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result, stack = [], []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left  # Move to leftmost node
            
            current = stack.pop()  # Process the node
            result.append(current.val)
            
            current = current.right  # Move to right subtree
        
        return result

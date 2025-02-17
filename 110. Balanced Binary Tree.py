# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1  # Unbalanced
            
            return max(left_height, right_height) + 1
        
        return height(root) != -1

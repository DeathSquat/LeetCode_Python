# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = [None]
        second = [None]
        prev = [None]

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # Find misplaced nodes
            if prev[0] and node.val < prev[0].val:
                if not first[0]:
                    first[0] = prev[0]  # First misplaced node
                second[0] = node  # Second misplaced node
            
            prev[0] = node  # Update prev node
            
            inorder(node.right)
        
        # Perform in-order traversal to detect swapped nodes
        inorder(root)
        
        # Swap values of the misplaced nodes
        if first[0] and second[0]:
            first[0].val, second[0].val = second[0].val, first[0].val

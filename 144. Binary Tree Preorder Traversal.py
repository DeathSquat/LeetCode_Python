# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Recursive approach
        result = []
        self.preorder(root, result)
        return result
    
    def preorder(self, node, result):
        if not node:
            return
        result.append(node.val)  # Visit root
        self.preorder(node.left, result)  # Traverse left
        self.preorder(node.right, result)  # Traverse right

# Iterative approach (using stack)
class SolutionIterative(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, result = [root], []
        
        while stack:
            node = stack.pop()
            result.append(node.val)  # Visit root
            
            if node.right:  # Push right child first
                stack.append(node.right)
            if node.left:  # Push left child last so it is processed first
                stack.append(node.left)
        
        return result

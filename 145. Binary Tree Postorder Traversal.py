# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive approach
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self.postorder(root, result)
        return result
    
    def postorder(self, node, result):
        if not node:
            return
        self.postorder(node.left, result)  # Traverse left
        self.postorder(node.right, result)  # Traverse right
        result.append(node.val)  # Visit root

# Iterative approach (using two stacks)
class SolutionIterative(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        stack, output = [root], []
        
        while stack:
            node = stack.pop()
            output.append(node.val)  # Visit root
            
            if node.left:  # Push left child
                stack.append(node.left)
            if node.right:  # Push right child
                stack.append(node.right)
        
        return output[::-1]  # Reverse the result to get postorder

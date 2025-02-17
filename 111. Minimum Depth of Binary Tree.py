# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0  # If tree is empty, depth is 0

        # If a node has only one child, we must take the non-null child's depth
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If both children exist, take the minimum of both depths
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

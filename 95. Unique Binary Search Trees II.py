# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0:
            return []
        
        return self.buildTrees(1, n)
    
    def buildTrees(self, start, end):
        if start > end:
            return [None]
        
        all_trees = []
        for root_val in range(start, end + 1):
            left_trees = self.buildTrees(start, root_val - 1)
            right_trees = self.buildTrees(root_val + 1, end)
            
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(root_val)
                    root.left = left
                    root.right = right
                    all_trees.append(root)
        
        return all_trees

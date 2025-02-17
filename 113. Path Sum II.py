# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(node, path, current_sum):
            if not node:
                return
            
            # Include the current node's value in the path
            path.append(node.val)
            current_sum += node.val
            
            # Check if it's a leaf node and the sum matches targetSum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(path))  # Make a copy of the path
            
            # Recur for left and right subtrees
            dfs(node.left, path, current_sum)
            dfs(node.right, path, current_sum)
            
            # Backtrack to explore other paths
            path.pop()
        
        dfs(root, [], 0)
        return result

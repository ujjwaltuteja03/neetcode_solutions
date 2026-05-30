# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def dfs(root):
            """no backtracking allowed
            only root is allowed to do a split"""

            """base case, return 0 when no children"""
            if not root: return 0

            """start collecting the max value 
            going only downwards from root node"""
            leftMax= dfs(root.left)
            rightMax= dfs(root.right)

            """in case of negative path, just take 0"""
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            """update res assuming the current node
            to be the only splitting point allowed.
            This makes sure that a subtree is also considered
            to be the split point"""
            res[0] = max(res[0], root.val+leftMax+rightMax) 

            """return the max of maximum left and right paths
            downwards to the leftMax and rightMax of the root
            that called this function recursively"""
            return root.val + max(leftMax,rightMax)
        dfs(root)
        return res[0]
#question: https://leetcode.com/problems/deepest-leaves-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        max_level = float('-inf')

        total = 0

        def dfs(root, level):

            nonlocal max_level
            nonlocal total

            if not root:

                return

            if root.left is None and root.right is None:

                if level == max_level:

                    total += root.val

                if level > max_level:

                    max_level = level
                    
                    total = root.val

            else:

                dfs(root.left, level + 1)
                dfs(root.right, level + 1)

        dfs(root, 0)

        return(total)

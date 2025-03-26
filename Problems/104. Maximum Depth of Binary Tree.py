# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_depth = 0

        def preorder(root, depth):
            nonlocal max_depth
            if not root:
                max_depth = max(max_depth, depth)
                return
            preorder(root.left, depth + 1)
            preorder(root.right, depth + 1)

        preorder(root, 0)
        return max_depth

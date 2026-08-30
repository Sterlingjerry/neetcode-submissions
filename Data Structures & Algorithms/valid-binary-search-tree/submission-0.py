# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def valid(self, node, lower, upper):
            # Empty subtree can't violate BST rules
            if node is None:
                return True

            # Current node must fit inside its allowed range
            if not (lower < node.val < upper):
                return False

            # Check both subtrees
            left_valid = self.valid(node.left, lower, node.val)
            right_valid = self.valid(node.right, node.val, upper)

            return left_valid and right_valid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Root starts with no restrictions
        return self.valid(root, float("-inf"), float("inf"))
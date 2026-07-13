# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestorHelper(self, root, p,q, smallest):
        smallest = root
        if p.val < root.val and q.val < root.val:
            smallest = self.lowestCommonAncestorHelper(root.left, p,q, smallest)
        if p.val > root.val and q.val > root.val:
            smallest = self.lowestCommonAncestorHelper(root.right, p,q, smallest)
        return smallest

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smallest = root
        return  self.lowestCommonAncestorHelper(root, p,q, smallest)
        
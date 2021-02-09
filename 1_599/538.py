# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def flat(dp, node):
            dp[node.val]= node.val
            if node.left:
                flat(dp, node.left)
            if node.right:
                flat(dp, node.right)
        if root == None:
            return None
        else:
            dp = {} #key is the value in the tree, since the value is unique
            flat(dp,root)
            lst = sorted(list(dp.keys()),reverse = True)
            arr=[lst[0]] #sum the larger elements in the tree

            for l in lst[1:]:
                arr.append(l+arr[-1])

            for i in range(len(lst)): #store the target value
                dp[lst[i]] = arr[i]

            def assign(dp, node):
                node.val = dp[node.val]
                if node.left:
                    assign(dp, node.left)
                if node.right:
                    assign(dp, node.right)

            assign(dp, root)
            return root



# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def convertBST(self, root: TreeNode) -> TreeNode:
#         def nxt(flat, node):
#             if node.left == node.right == None:
#                 flat.append(node.val)
#             else:
#                 flat.append(node.val)
#                 if node.left:
#                     nxt(flat, node.left)
#                 if node.right:
#                     nxt(flat, node.right)
#
#         if root == None: return None
#         flat = []
#         nxt(flat, root)
#         s = sorted(list(set(flat)))
#         hmp = {}
#         for i in range(len(s)):
#             if s[i] not in hmp:
#                 hmp[s[i]] = sum(s[i:])
#
#         def compute(hmp, node):
#             node.val = hmp[node.val]
#             if node.left:
#                 compute(hmp, node.left)
#             if node.right:
#                 compute(hmp, node.right)
#
#         compute(hmp, root)
#         return root

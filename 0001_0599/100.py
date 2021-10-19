# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def flat(n1, n2):
            if n1.val != n2.val:
                return False
            else:
                if n1.left and n2.left:
                    if flat(n1.left, n2.left) == False:
                        return False
                elif (n1.left and n2.left == None or n1.left == None and n2.left):
                    return False
                if n1.right and n2.right:
                    if flat(n1.right, n2.right) == False:
                        return False
                elif (n1.right and n2.right == None or n1.right == None and n2.right):
                    return False
                return True

        if p == q == None:
            return True
        else:
            if (p == None and q) or (p and q == None):
                return False
            else:
                return flat(p, q)


# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         def flat(node, output, curr):
#             if node.left == node.right == None:
#                 output.append(curr + [None, None])
#             else:
#                 if node.left and node.right:
#                     flat(node.left, output, curr + [node.left.val])
#                     flat(node.right, output, curr +[node.right.val])
#                 elif node.left:
#                     flat(node.left, output, curr + [node.left.val] + [None])
#                 elif node.right:
#                     flat(node.right, output, curr + [None] + [node.right.val])
#         if p == q == None: return True
#         else:
#             if (p==None and q!=None) or (p!=None and q==None): return False
#             else:
#                 output_p = []
#                 flat(p, output_p, [p.val])
#                 output_q = []
#                 flat(q, output_q, [q.val])
#                 return output_p == output_q



# previous approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         def dfs(node, curr):  # curr is curr path
#             if node:
#                 if node.left == node.right == None:
#                     return curr
#                 else:
#                     if node.left != None:
#                         curr.append(node.left.val)
#                         dfs(node.left, curr)
#                     else:
#                         curr.append(None)
#
#                     if node.right != None:
#                         curr.append(node.right.val)
#                         dfs(node.right, curr)
#                     else:
#                         curr.append(None)
#
#         if p == None and q == None:
#             return True
#         elif p != None and q != None:
#             curr_1 = [p.val]
#             dfs(p, curr_1)
#             curr_2 = [q.val]
#             dfs(q, curr_2)
#             return True if curr_1 == curr_2 else False
#         else:
#             return False  # p!=None, q==None or vice versa
